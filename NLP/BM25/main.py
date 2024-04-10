import math
import jieba

import re

text = '''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
'''

class BM25(object):

    def __init__(self, docs):
        self.D = len(docs) # doc个数
        self.avgdl = sum([len(doc)+0.0 for doc in docs]) / self.D # 每篇平均长度
        self.docs = docs
        self.f = []  # 列表的每一个元素是一个dict，dict存储着一个文档中每个词的出现次数
        self.df = {} # 存储每个词及出现了该词的文档数量(count)
        self.idf = {} # 存储每个词的idf值，当作权重
        self.k1 = 1.5
        self.b = 0.75
        self.init()

    def init(self):
        for doc in self.docs:
            tmp = {}
            for word in doc:
                tmp[word] = tmp.get(word, 0) + 1  # 存储每个文档中每个词的出现次数（也可以用defaultdict)
            self.f.append(tmp) # idx为索引，f[idx]为一个dict，dict存储着第idx+1个文档中每个词的出现次数,idx代表第几个文档。
            for k in tmp.keys(): # 如果词k出现在了当前文档中，则df[k]即文档数量加1
                self.df[k] = self.df.get(k, 0) + 1
        for k, v in self.df.items():
            self.idf[k] = math.log(self.D-v+0.5)-math.log(v+0.5) # 计算idf

    def sim(self, query, index): # 与单个文档的相似度
        score = 0
        for word in query:
            if word not in self.f[index]:
                continue
            d = len(self.docs[index]) # 当前文档的长度
            score += (self.idf[word]*(self.f[index][word]/d)*(self.k1+1)
                      / ((self.f[index][word]/d)+self.k1*(1-self.b+self.b*d
                                                      / self.avgdl)))
        return score

    def simall(self, query):
        scores = []
        for index in range(self.D):
            score = self.sim(query, index)
            scores.append(score)
        return scores
    
def get_sentences(doc):
    line_break = re.compile('[\r\n]') # 以换行符分割
    delimiter = re.compile('[，。？！；]') # 以中文标点符号分割
    sentences = []
    for line in line_break.split(doc):
        line = line.strip()
        if not line:
            continue
        for sent in delimiter.split(line):
            sent = sent.strip()
            if not sent:
                continue
            sentences.append(sent)
    return sentences

if __name__ == '__main__':
    sents = get_sentences(text)
    print(sents)
    doc = []
    for sent in sents:
        words = list(jieba.cut(sent))
        doc.append(words)
    # print(doc)
    s = BM25(doc)
    # print(s.f)
    # print(s.df)
    # print(s.idf)
    print(s.simall(['自然语言', '计算机科学', '领域', '人工智能', '领域']))