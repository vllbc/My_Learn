<<<<<<< HEAD
from itertools import dropwhile, takewhile
# 你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们，用dropwhile

with open('testvim.txt', 'r') as fp:
    for i in dropwhile(lambda i: i.startswith("#"), fp):  # 跳过前面#号开头的
        print(i)

with open("testvim.txt", "r") as fp:
    # 遍历带#号开头的，遇到不是#号开头的就退出循环，可以当做break使用
    for i in takewhile(lambda i: i.startswith("#"), fp):
        # 相当于 if not i.startwith("#"): break
        print(i)
        
=======
from itertools import dropwhile,takewhile
# 你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们，用dropwhile

with open('testvim.txt','r') as fp:
    for i in dropwhile(lambda i:i.startswith("#"),fp): # 跳过前面#号开头的
        print(i)

with open("testvim.txt","r") as fp:
    for i in takewhile(lambda i:i.startswith("#"),fp): # 遍历带#号开头的，遇到不是#号开头的就退出循环，可以当做break使用
        # 相当于 if not i.startwith("#"): break
        print(i)
>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf
