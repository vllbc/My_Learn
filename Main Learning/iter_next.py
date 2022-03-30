class Range7: # 可迭代类型 只需要实现__iter__即可
    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end
    def __iter__(self):
        return Range7iterator(self)
        


class Range7iterator: #这是迭代器,一般的迭代器只能调用一次
    def __init__(self,rangeobj) -> None:
        self.rangeobj = rangeobj
        self.cur = rangeobj.start

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.cur > self.rangeobj.end:
                raise StopIteration
            if self.is_7(self.cur):
                res = self.cur
                self.cur += 1
                return res
            self.cur += 1
    def is_7(self,num):
        if num == 0:
            return False
        return num%7==0 or "7" in str(num)
for i in Range7(1,100):
    print(i,end=" ")

#可迭代对象不一定是迭代器，但迭代器一定是可迭代对象

# 对可迭代对象使用 iter() 会返回迭代器，迭代器则会返回它自身

# 每个迭代器的被迭代过程是一次性的，可迭代对象则不一定

# 可迭代对象只需要实现 __iter__ 方法，而迭代器要额外实现 __next__ 方法