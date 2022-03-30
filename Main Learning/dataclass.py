from dataclasses import dataclass
import random


@dataclass(order=True) # 等于实现了各种比较方法例如=、>、<,排序函数都依赖比较两个对象
class A:
    n: int


nums = [A(random.randint(1,10)) for _ in range(10)]
nums = sorted(nums)
print(nums, end='')
x = '''hello'''
print(x)



# from dataclasses import dataclass
# @dataclass(unsafe_hash=True)
# class VisitRecordDC:
#     first_name: str
#     last_name: str
#     phone_number: str
#     # 跳过“访问时间”字段，不作为任何对比条件
#     date_visited: str = field(hash=False, compare=False)


# def find_potential_customers_v4():
#     return set(VisitRecordDC(**r) for r in users_visited_phuket) - \ 求差集
#         set(VisitRecordDC(**r) for r in users_visited_nz)
