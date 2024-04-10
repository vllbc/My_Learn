import numpy as np
import matplotlib.pyplot as plt

center = np.array([[0, 0], [0, 1]])
cls_num = 2  # 类别的数目
X = np.array([[0, 0], [0, 1], [2, 1], [2, 3], [3, 4], [1, 0]])  # 数据集
max_iter = 10  # 最大迭代次数
cls = np.zeros(X.shape[0])  # 每一个坐标对应一个类别
run = True
while run and max_iter > 0:
    for i, x in enumerate(X):
        tmp = np.argmin(np.sum(np.power(x - center, 2), axis=1))
        cls[i] = tmp
    run = False
    print(cls)
    # 重新计算聚类中心
    for i in range(cls_num):
        data = X[cls == i]  # 取相同类别的样本
        new_center = np.mean(data, axis=0)  # 对于相同类别的x坐标y坐标求平均值
        if np.sum(np.abs(center[i]-new_center), axis=0) > 1e-4:
            center[i] = new_center  # 更新中心
            run = True
    max_iter -= 1
plt.scatter(X[:, 0], X[:, 1], c=cls)
plt.show()

