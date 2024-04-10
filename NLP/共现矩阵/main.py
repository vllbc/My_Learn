import numpy as np
def Co_currence_matrix(words, num_words, corpus, window_size):
    word2ind = {w: i for i, w in enumerate(words)} # word到key，words就是词汇表
    M = np.zeros((num_words, num_words)) # num_words是词汇表的长度

    for c in corpus: # 假设语料库是一个列表，元素为一段文本。遍历语料库
    
        for idx, word in enumerate(c): # 遍历文本的每一个词，这里默认空格分词

            for i in range(1, window_size+1): # 对窗口大 小进行遍历

                left = idx - i # 自己与自己不算共现，所以这里要加减

                right = idx + i

                if left >= 0: # 左边元素

                    M[word2ind[word], word2ind[c[left]]] += 1

                if right < len(c): # 右边元素

                    M[word2ind[word], word2ind[c[right]]] += 1