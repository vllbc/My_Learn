
n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))

import collections
hashs = collections.defaultdict(list)
for i in range(n):
    for j in range(n):
        hashs[j + i].append(mat[i][j])
flag = True
res = []
for k,v in sorted(hashs.items()):
    if flag:
        res.extend(v[::-1])
    else:
        res.extend(v)
    flag = not flag
print(" ".join(map(str,res)))