from collections import defaultdict


m = defaultdict(int)
m[1] += 1

n = dict()
n[1] += 1 # 报错
print(m)
print(n)