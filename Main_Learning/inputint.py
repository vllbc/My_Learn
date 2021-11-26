from typing import Iterable
from pydantic import BaseModel,conint,ValidationError


class NumberInput(BaseModel):
    num: conint(ge=0, le=100)


def input_a_number():
    while True:
        n = input("输入一个数")
        try:
            n = NumberInput(num=n)
        except ValidationError as e:
            print(e)
            continue
        n = n.num
        break
    return n

print(input_a_number())
            