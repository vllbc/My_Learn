import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from textblob import TextBlob
from jieba import analyse

data_path = "./titles.csv" # 数据文件路径
n = 3 # 聚类个数

def read_data():
    """

    Returns:
        data: 原始数据
    """
    data = pd.read_csv(data_path)
    data.dropna(inplace=True)
    data = data.values.flatten()
    return data

def calc_weights(data):
    """

    Args:
        data : 原始数据

    Returns:
        weights: 计算好的权重
    """
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(data)
    return tfidf.toarray()

def decomposition(weights, n_components=5):
    """
    Args:
        weights : 还没降维的权重
        n_components (int, optional): 需要降到的维数 Defaults to 2.

    Returns:
        weights: 降维后的权重
    """
    pca = PCA(n_components=n_components)
    weights = pca.fit_transform(weights)
    return weights

def train(weights):
    """

    Args:
        weights : 降维后的权重

    Returns:
        KMeans: 训练好的kmeans模型
    """
    kmeans = KMeans(n_clusters=n).fit(weights)
    return kmeans

def save(data, kmeans):
    """聚类并保存结果

    Args:
        data (List): 原始数据
        kmeans (model): 训练好的聚类模型
    """
    center_l = kmeans.cluster_centers_
    labels = kmeans.labels_
    n_clusters = len(center_l)
    
    cluster_menmbers_list = []

    for i in range(n_clusters):
        menmbers_list = []
        for j in range(0, len(labels)):
            if labels[j] == i:
                menmbers_list.append(j)
        cluster_menmbers_list.append(menmbers_list)
        
    for i in range(len(cluster_menmbers_list)):
        with open(f"{i}.txt", "a+", encoding="utf-8") as f:
            f.write("                 \n")
            for j in range(0, len(cluster_menmbers_list[i])):
                a = cluster_menmbers_list[i][j]
                f.write(data[a] + '\n')   

def rewrite():
    """
    将关键词写入文件
    """
    for i in range(n):
        with open(f"{i}.txt", "r+", encoding="utf-8") as fp:
            content = fp.read()
            # blob = TextBlob(content)
            # keywords = ",".join(blob.noun_phrases[:10]) # 十个关键词
            keywords = ",".join(analyse.extract_tags(content, topK=10)) # 十个关键词
            fp.seek(0, 0)
            fp.write("keyword:" + keywords + "\n")

# 主程序
if __name__ == "__main__":
    data = read_data()
    weights = calc_weights(data)
    weights = decomposition(weights)
    kmeans = train(weights)
    save(data, kmeans)
    rewrite()