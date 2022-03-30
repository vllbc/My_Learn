# 手动实现一下enumerate
from typing import Iterable
def enumerate_(Iterable:Iterable,start=0):
    yield from zip(range(start,start+len(Iterable)),Iterable)

for i,item in enumerate_([1,2,3,4,5,6],9):
    print(i,item)
