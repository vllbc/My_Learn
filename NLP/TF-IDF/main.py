corpus = ['this is the first document',
            'this is the second second document',
            'and the third one',
            'is this the first document']
words_list = list()
for i in range(len(corpus)):
    words_list.append(corpus[i].split(' '))
## python手动实现
def manual():
    
    from collections import Counter
    count_list = list()
    for i in range(len(words_list)):
        count = Counter(words_list[i])
        count_list.append(count)

    import math
    def tf(word, count):
        return count[word] / sum(count.values())


    def idf(word, count_list):
        n_contain = sum([1 for count in count_list if word in count])
        return math.log(len(count_list) / (1 + n_contain))


    def tf_idf(word, count, count_list):
        return tf(word, count) * idf(word, count_list)

    for i, count in enumerate(count_list):
        print("第 {} 个文档 TF-IDF 统计信息".format(i + 1))
        scores = {word : tf_idf(word, count, count_list) for word in count}
        sorted_word = sorted(scores.items(), key = lambda x : x[1], reverse=True)
        for word, score in sorted_word:
            print("\tword: {}, TF-IDF: {}".format(word, round(score, 5)))

def gensim_work():
    from gensim import corpora
    # 赋给语料库中每个词(不重复的词)一个整数id
    dic = corpora.Dictionary(words_list) # 创建词典
    new_corpus = [dic.doc2bow(words) for words in words_list]
    # 元组中第一个元素是词语在词典中对应的id，第二个元素是词语在文档中出现的次数
    from gensim import models
    tfidf = models.TfidfModel(new_corpus)
    tfidf.save("tfidf.model")
    # 载入模型 
    tfidf = models.TfidfModel.load("tfidf.model")
    # 使用这个训练好的模型得到单词的tfidf值
    res = [tfidf[temp] for temp in new_corpus]
    print(res)

def sklearn_work():
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)
    print(tfidf.toarray()) # 权重
    # print(vectorizer.get_feature_names()) # 单词
    # print(vectorizer.vocabulary_) # 词典
manual()
gensim_work()
sklearn_work()