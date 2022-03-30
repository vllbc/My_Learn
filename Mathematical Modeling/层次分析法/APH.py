# 层次分析法
import numpy as np

RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}

A = [[1, 1/2, 4, 3, 3],
 [2, 1, 7, 5, 5],
 [1/4, 1/7, 1, 1/2, 1/3],
 [1/3, 1/5, 2, 1, 1],
 [1/3, 1/5, 3, 1, 1]]
n = len(A)
# 算数平均法求权重
Sum_A = np.sum(A, axis=0, keepdims=True)
print("算数平均值法：")
print(np.sum(A / Sum_A, axis=1) / n)
print("")

# 几何平均法求权重
mul = np.prod(A, axis=1)
temp = mul ** (1/n)
print(temp / np.sum(temp))

# 特征值法求权重
d,v = np.linalg.eig(A) # d为特征值，v为特征向量
Max_eig = np.max(d)
c = np.where(d == Max_eig)[0]
print("特征值法：")
res = v[:, c] / sum(v[:, c])
print(np.squeeze(res))


CI = (Max_eig - n) / (n - 1)
RI = RI_dict[n]
CR = CI / RI
if CR < 0.1:
    print(f"CR的值为{CR}，一致性可以接受")
else:
    print(f"CR的值为{CR}，一致性不可以接受")

