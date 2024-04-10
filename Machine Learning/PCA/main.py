# 手动实现PCA算法
import numpy as np

def pca(data):
    """
    主成分分析
    :param data: 数据集
    :return:
    """
    # 数据集的行数
    num_data, num_feat = data.shape
    # 对每一列的数据进行平均值的计算
    mean_vec = np.mean(data, axis=0)
    # 对数据集中每一行的数据进行平均值的计算
    data_mean_centered = data - mean_vec
    # 计算协方差矩阵
    sigma = np.dot(data_mean_centered.T, data_mean_centered) / num_data 
    # 计算特征值和特征向量
    eig_val, eig_vec = np.linalg.eig(sigma)
    # 对特征值进行排序
    eig_pairs = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(len(eig_val))]
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    # 要降维的维数，这里以2为例。将特征向量以列向量形式拼合。
    matrix_w = np.hstack([eig_pairs[i][1].reshape(-1, 1) for i in range(2)])
    # 将原始数据进行投影。
    res = data.dot(matrix_w)
    print(res)
pca(np.array([[1, 2, 5], [3, 4, 6], [5, 6, 9], [3, 2 ,5]]))