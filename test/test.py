from pydantic import BaseModel 



class Test():
    def __init__(self, n: int) -> None:
       self.n = n 
    
    def __repr__(self) -> str:
        return str(self.n)

    __str__ = __repr__

test1 = Test(1)
print(test1)