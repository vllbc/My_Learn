from enum import IntEnum

class Test(IntEnum):
    X = 2
    Y = 1

print(2 == Test.X)