<<<<<<< HEAD
n = eval(input("输入要打印的行数："))
triangle = [[1], [1, 1]]
for i in range(2, n):
    pre = triangle[i-1]
    cul = [1] 
    for j in range(i-1): 
        cul.append(pre[j]+pre[j+1])
    cul.append(1)
    triangle.append(cul)
for i in range(n): 
    s = " "*(n-i-1)
    for j in triangle[i]:
        s = s + str(j)+" "
    print(s)
=======
import numpy as np
arr1 = np.random.randint(1,10,(3,4))
>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf
