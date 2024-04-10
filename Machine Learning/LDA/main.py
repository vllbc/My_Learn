import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = pd.read_csv("./water.csv")
data.dropna(inplace=True)
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

ss = StandardScaler()
X = ss.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=553)

class_num = 2
mean_list = []
for i in range(class_num):
    mean_list.append(np.mean(X_train[y_train==i], axis=0))
mean_list = np.array(mean_list)
S_W = np.zeros((X_train.shape[1], X_train.shape[1])) # 类内散度矩阵
for c, mv in zip(range(class_num), mean_list):
    class_scatter = np.zeros((X_train.shape[1], X_train.shape[1]))
    for row in X_train[y_train==c]:
        row, mv = row.reshape(X_train.shape[1], -1), mv.reshape(X_train.shape[1], -1)
        class_scatter += (row-mv).dot((row-mv).T)
    S_W += class_scatter

over_all_mean = np.mean(X_train, axis=0)
S_B = np.zeros((X_train.shape[1], X_train.shape[1])) # 类间散度矩阵
for i, mean_vec in enumerate(mean_list):
    n = X_train[y_train==i, :].shape[0]
    mean_list_temp = mean_list[i, :].reshape(1, -1)
    over_all_mean = over_all_mean.reshape(X_train.shape[1], 1)
    S_B += n*(mean_vec-over_all_mean).dot((mean_vec-over_all_mean).T)


eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]
 

eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)
# eigv_sum = sum(eig_vals)
# for i, j in enumerate(eig_pairs):
#     print('eigenvalue {0:}: {1:.2%}'.format(i + 1, (j[0] / eigv_sum).real)) # 根据百分比显示特征值，从而选取最大的n个特征值
W = np.hstack((eig_pairs[0][1].reshape(X_train.shape[1], 1), eig_pairs[1][1].reshape(X_train.shape[1], 1)))
print(X_train @ W)