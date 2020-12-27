s = "abba"
t = 'abab'
from collections import defaultdict

d1 = defaultdict(list)
d2 = defaultdict(list)

for k,i in enumerate(s):
    d1[i].append(k)
for k,i in enumerate(t):
    d2[i].append(k)
if len(d1) != len(d2):
    print(False)
for k1,k2 in zip(d1.keys(),d2.keys()):
    if d1[k1] != d2[k2]:
        print(False)
print(True)
