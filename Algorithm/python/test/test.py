res = []
text,n = input().split()
t = input().split()
from fnmatch import fnmatch

for s in t:
    if fnmatch(s,text):
        res.append(s)
if res != []:
    print(' '.join(res))
else:
    print("no")