from pydantic import BaseModel


class Test():

    def __init__(self, cls, n):
        self.cls = cls
        self.n = n 
    @property
    def to_string(self):
        return self.cls
    
    @property
    def to_strings(self):
        return self.n


class Test_For(BaseModel):
    num: int

    def __str__(self):
        return str(self.num)
    
    __repr__ = __str__

test = Test(Test_For, 22)
print(test.to_string(num=1))
print(test.to_strings)