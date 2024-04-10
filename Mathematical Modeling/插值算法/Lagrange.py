# 拉格朗日插值法

import numpy as np
import random
import matplotlib.pyplot as plt


def getdata():
    a = np.linspace(-255, 255, 10)
    b = np.linspace(-255, 255, 10)
    return a, b


x, y = getdata()


def lagrange(x, y, xn):
    ans = 0.0
    for i in range(len(x)):
        L = 1.0
        for j in range(len(x)):
            if i != j:
                L *= (xn - x[j]) / (x[i] - x[j])
        ans += L * y[i]
    return ans


xn = np.arange(-255, 255, 1)
yn = np.zeros(len(xn))
<<<<<<< HEAD
print(xn)
=======
>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf

for i in range(len(xn)):
    yn[i] += lagrange(x, y, xn[i])
plt.plot(x, y, "r*")
plt.plot(xn, yn, "-")
plt.show()
