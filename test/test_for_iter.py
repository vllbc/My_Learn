# import random
# from re import T


# class Test:
#     def __init__(self) -> None:
#         pass

#     def __call__(self):
#         return random.randint(1,10)


# for i in iter(Test(), 5): #如果遇到5则直接退出迭代
#     pass

# class Node:
#     def __init__(self,value) -> None:
#         self._value = value
#         self._node = []
    
#     def __repr__(self) -> str:
#         return f'Node({self._value})'
    
#     def add_children(self,node:'Node') -> 'Node':
#         self._node.append(node)
    
#     def __iter__(self):
#         return iter(self._node)

#     def dfs(self):
#         yield self
#         for i in self:
#             yield from i.dfs()
# root = Node(0)
# children1 = Node(1)
# children2 = Node(2)
# root.add_children(children1)
# root.add_children(children2)
# children1.add_children(Node(3))
# children1.add_children(Node(4))
# children11 = Node(5)
# children2.add_children(children11)
# children11.add_children(Node(6))
# for c in root.dfs():
#     print(c)


# class CountDown:
#     def __init__(self,start) -> None:
#         self.start = start
    
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
    
#     def __reversed__(self):
#         n = 1
#         while n <= self.start:
#             yield n
#             n += 1

# iters = CountDown(5)
# # 正向遍历
# for i in iters:
#     print(i)

# print()
# # 反向遍历
# for i in reversed(iters):
#     print(i)

# from itertools import islice

# def test():
#     t = 0
#     while True:
#         yield t
#         t += 1

# for i in islice(test(),10,20):
#     print(i)


# from itertools import dropwhile

# with open('./test/testvim.txt','r') as fp:
#     for i in dropwhile(lambda i:i.startswith("#"),fp):
#         print(i)


# # 手动实现一下enumerate
# from typing import Iterable
# def enumerate_(Iterable:Iterable,start=0):
#     yield from zip(range(start,start+len(Iterable)),Iterable)

# for i,item in enumerate_([1,2,3,4,5,6],9):
#     print(i,item)

from itertools import chain

lists = [[1,2,3],[4,5],[6]]
print(sum(lists,[]))
print([i for j in lists for i in j])
print(list(chain(*lists)))
from typing import Iterable
def flatten(items,ignore=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore):
            yield from flatten(x)
        else:
            yield x
print(list(flatten(lists)))