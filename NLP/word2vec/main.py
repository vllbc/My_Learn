import logging
import pickle
import torch.nn.functional as F
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data as Data
from collections import Counter
import random

import copy

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

C = 5 # window size
K = 15  # Number of negitive samples
epochs = 1
MAX_VOCAB_SIZE = 10000 # 单词表的长度
EMBEDDING_SIZE = 100 # 词嵌入的维数
batch_size = 32 
lr = 1e-3

with open("./text8/text8.train.txt", "r") as f:
    text = f.read()
text = text.lower().split()

vocab_dict = dict(Counter(text).most_common(MAX_VOCAB_SIZE-1))
vocab_dict["<UNK>"] = len(text) - np.sum(list(vocab_dict.values()))

word2idx = {word: i for i, word in enumerate(vocab_dict.keys())}
idx2word = {i: word for i, word in enumerate(vocab_dict.keys())}

word_counts = np.array([count for count in vocab_dict.values()])
word_freqs = word_counts / np.sum(word_counts)
word_freqs = word_freqs ** (3/4)  # 经验


class WordEmbeddingDataset(Data.Dataset):
    def __init__(self, text, word2idx, word_freqs):
        super(WordEmbeddingDataset, self).__init__()
        self.text_encoded = torch.LongTensor(
            [word2idx.get(word, word2idx["<UNK>"]) for word in text]) # 得到wordid，没有则为unk的id
        self.word2idx = word2idx
        self.word_freqs = torch.Tensor(word_freqs)

    def __getitem__(self, index):
        center_words = self.text_encoded[index]
        pos_indices = list(range(index-C, index)) + \
            list(range(index+1, index+C+1))
        pos_indices = [i % len(self.text_encoded) for i in pos_indices]
        pos_words = self.text_encoded[pos_indices]
        select_weights = copy.deepcopy(self.word_freqs)
        select_weights[center_words] = 0
        select_weights[pos_words] = 0
        neg_words = torch.multinomial(
            select_weights, K * pos_words.shape[0], True)
        return center_words, pos_words, neg_words

    def __len__(self):
        return len(self.text_encoded)

dataset = WordEmbeddingDataset(text, word2idx, word_freqs)
dataloader = Data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

class Model(nn.Module):
    def __init__(self, vocab_size, embedding_size):
        super(Model, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_size)
        self.embedding2 = nn.Embedding(vocab_size, embedding_size)
    
    def forward(self, input_lables, pos_labels, neg_labels):
        input_embedding = self.embedding(input_lables) # [batch_size, embedding_size]
        pos_embedding = self.embedding2(pos_labels) # [batch_size, window * 2, embedding_size]
        neg_embedding = self.embedding2(neg_labels) # [batch_size, K * window * 2, embedding_size]
        
        input_embedding = input_embedding.unsqueeze(2) # [batch_size, embedding_size, 1]
        
        pos_dot = torch.bmm(pos_embedding, input_embedding).squeeze(2) # [batch_size, window * 2]
        ## bmm == batch matrix multiply
        neg_dot = torch.bmm(neg_embedding, input_embedding).squeeze(2) # [batch_size, K * window * 2]
        
        log_pos = F.logsigmoid(pos_dot).sum(dim=1) # [batch_size]
        log_neg = F.logsigmoid(-1 * neg_dot).sum(dim=1) # [batch_size]

        return -(log_pos + log_neg).mean() # 对应上文推导的公式
    
    def input_embedding(self):
        return self.embedding.weight.detach().cpu().numpy()

model = Model(MAX_VOCAB_SIZE, EMBEDDING_SIZE).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=lr) # 参数为模型参数和学习率

for epoch in range(epochs):
    for i, (input_labels, pos_labels, neg_labels) in enumerate(dataloader):
        input_labels = input_labels.long().to(device)
        pos_labels = pos_labels.long().to(device)
        neg_labels = neg_labels.long().to(device)
        optimizer.zero_grad() # 梯度清零
        loss = model(input_labels, pos_labels, neg_labels)
        loss.backward() # 反向传播
        optimizer.step() # 利用梯度下降更新参数 
        if (i+1) % 100 == 0:
            logging.info(f"epoch: {epoch}, batch: {i+1}, loss: {loss.item()}")

embedding_weights = model.input_embedding()
torch.save(model.state_dict(), f"embedding-{EMBEDDING_SIZE}.pth")
with open("word2idx.pkl", "wb") as f:
    pickle.dump(word2idx, f)

with open("idx2word.pkl", "wb") as f:
    pickle.dump(idx2word, f)

with open("embedding_weights.pkl", "wb") as f:
    pickle.dump(embedding_weights, f)