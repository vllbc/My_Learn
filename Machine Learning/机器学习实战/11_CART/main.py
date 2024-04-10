
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
#要聚类的数据
corpus = [
    'This is the first document.',#0
    'This is the second second document.',#1
    'And the third one.',#2
    'Is this the first document?',#3
    'I like reading',#4
    'do you like reading?',#5
    'how funny you are! ',#6
    'he is a good guy',#7
    'she is a beautiful girl',#8
    'who am i',#9
    'i like writing',#10
    'And the first one',#11
    'do you play basketball',#12
]
#将文本中的词语转换为词频矩阵
vectorizer = CountVectorizer()
#计算个词语出现的次数
X = vectorizer.fit_transform(corpus)#获取词袋中所有文本关键词
word = vectorizer.get_feature_names()

#类调用
transformer = TfidfTransformer()

#将词频矩阵X统计成TF-IDF值
tfidf = transformer.fit_transform(X)
#查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
weight = tfidf.toarray()
# print weight

# kmeans聚类
from sklearn.cluster import KMeans

# print data
kmeans = KMeans(n_clusters=5, random_state=0).fit(weight)#k值可以自己设置，不一定是五类
# print kmeans
centroid_list = kmeans.cluster_centers_
labels = kmeans.labels_
n_clusters_ = len(centroid_list)
# print "cluster centroids:",centroid_list
print(labels)
max_centroid = 0
max_cluster_id = 0
cluster_menmbers_list = []

for i in range(0, n_clusters_):

    menmbers_list = []
    for j in range(0, len(labels)):
        if labels[j] == i:
            menmbers_list.append(j)
    cluster_menmbers_list.append(menmbers_list)
# print cluster_menmbers_list
#聚类结果
for i in range(0,len(cluster_menmbers_list)):
    print('第' + str(i) + '类' + '---------------------')
    for j in range(0,len(cluster_menmbers_list[i])):
       a = cluster_menmbers_list[i][j]
       print(corpus[a])