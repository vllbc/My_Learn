from functools import reduce

x,n = input().split()
x,n = float(x),int(n)
res = 1.0
ji = lambda x,y: x * y

for i in range(1,n + 1):
    res += (x ** i) / reduce(ji,range(1,i+1))
print("{:.6f}".format(res))
