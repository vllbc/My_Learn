import pickle
import scipy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
with open("./embedding_weights.pkl", "rb") as f:
    embedding_weights = pickle.load(f)
with open("./word2idx.pkl", "rb") as f:
    word2idx = pickle.load(f)

with open("./idx2word.pkl", "rb") as f:
    idx2word = pickle.load(f)
def find_nearest(word):
    idx = word2idx[word]
    embedding = embedding_weights[idx]
    cosdis = np.array([scipy.spatial.distance.cosine(e, embedding) for e in embedding_weights])
    return [idx2word[i] for i in np.argsort(cosdis)[:10]]
print(find_nearest("two"))