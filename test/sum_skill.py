from pydantic import BaseModel
from functools import reduce
from typing import Sequence


class Test(BaseModel):
    text: Sequence[str]

    @classmethod
    def create(cls,text: Sequence[str]) -> "Test":
        return cls(text=text)
    
    def to_tuple(self) -> "Test":
        return Test(text=tuple(self.text))

    @classmethod
    def join(cls, *Tests):
        # return cls.create(sum([i.text for i in Tests],[]))
        return cls.create(reduce(lambda x,y:x+y, [i.text for i in Tests]))

test = Test.create(list("Hello world"))
t2 = Test.create(list("NIHAO"))
print(Test.join(test, t2))
