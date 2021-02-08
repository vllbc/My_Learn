import random
from re import T


class Test:
    def __init__(self) -> None:
        pass

    def __call__(self):
        return random.randint(1,10)

for i in iter(Test(), 5): #如果遇到5则直接退出迭代
    print(i)