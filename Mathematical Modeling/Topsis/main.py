import pandas as pd
import numpy as np

# 对极小型指标进行处理
def Min2Max(data):
    return data.max() - data

# 对中间型指标进行处理
def Mid2Max(data, best):
    M = np.max(np.abs(data-best))
    return 1 - np.abs(data-best)/M

# 对区间型指标进行处理
def Inter2Max(data, a, b):
    row = data.shape[0]
    M = max([a - np.min(data), np.max(data) - b])
    res = np.zeros(row)
    for i in range(row):
        if data[i] < a:
            res[i] = 1 - (a - data[i])/M
        elif data[i] > b:
            res[i] = 1 - (data[i] - b)/M
        else:
            res[i] = 1
    return res
data = pd.read_excel("20条河流的水质情况数据.xlsx").values

# 原始矩阵正向化
data[:, 3] = Min2Max(data[:, 3])
data[:, 2] = Mid2Max(data[:, 2], 7)
data[:, 4] = Inter2Max(data[:, 4], 10 ,20)


# 正向化矩阵标准化
data[:, 1:] = data[:, 1:] / np.sum(data[:, 1:]**2, axis=0)**0.5

# 计算得分并归一化
temp = data[:, 1:]
Z_zheng = np.max(temp, axis=0)
Z_fu = np.min(temp, axis=0)
w = np.ones(temp.shape[1]) # 在这里修改权重
D_zheng = np.sum(w*(Z_zheng-temp)**2, axis=1)**0.5  
D_fu = np.sum(w*(Z_fu-temp)**2, axis=1)**0.5  
S = D_fu / (D_zheng + D_fu)
Stand_S = S / np.sum(S)

# 降序排列
inx = np.argsort(-Stand_S)
Stand_S = Stand_S[inx]
print(Stand_S)
