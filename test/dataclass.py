from dataclasses import dataclass
import random


@dataclass(order=True)
class A:
    n: int


nums = [A(random.randint(1,10)) for _ in range(10)]
nums = sorted(nums)
print(nums, end='')
x = '''hello'''
print(x)