# import matplotlib.pyplot as plt
# import numpy as np
# font = {"color":"red","size":15}
# ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])
# plt.plot(ypoints,marker="o",color="r",linestyle="-.")
# plt.title("test",fontdict=font,loc="center")
# plt.xlabel("x",fontdict=font)
# plt.ylabel("y",fontdict=font)
# plt.grid(axis="x")
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
xpoints = np.array([0, 6])
ypoints = np.array([0, 100])

plt.subplot(1, 2, 1)
plt.plot(xpoints,ypoints)
plt.title("plot 1")

#plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("plot 2")

plt.suptitle("RUNOOB subplot Test")
plt.show()