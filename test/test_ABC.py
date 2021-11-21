# from abc import ABC,abstractmethod
# import logging


# class AbsLogger(ABC):
#     @abstractmethod
#     def info(self, msg):
#         pass

#     @abstractmethod
#     def debug(self, msg):
#         pass

#     @abstractmethod
#     def error(self, msg):
#         pass

#     @abstractmethod
#     def warn(self, msg):
#         pass

#     @abstractmethod
#     def exception(self, msg):
#         pass

# class LogingLogger(AbsLogger):
#     def __init__(self) -> None:
#         logging.basicConfig(
#             format="[%(asctime)s][%(levelname)s]: %(message)s", level=logging.DEBUG
#         )
    
#     def info(self, msg):
#         return logging.info(msg)
    
#     def debug(self, msg):
#         return logging.debug(msg)
    
#     def error(self, msg):
#         return logging.error(msg)
    
#     def warn(self, msg):
#         return logging.warn(msg)
    
#     def exception(self, msg):
#         return logging.exception(msg)

# class Test(LogingLogger):
#     def info(self, msg):
#         super().info(msg)
#         print("info")
    
#     def debug(self, msg):
#         super().info(msg)
#         print("debug")
    
#     def error(self, msg):
#         super().info(msg)
#         print("error")
    
#     def warn(self, msg):
#         super().info(msg)
#         print("warn")
    
#     def exception(self, msg):
#         super().info(msg)
#         print("exception")
    
# T = Test()
# T.info("1")

import collections
from abc import ABC, abstractmethod
from typing import List

customer = collections.namedtuple('customer', ['name', 'points'])


class Goods():
    def __init__(self, name: str, quantity: float, price: float) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price

    def total(self) -> float:
        return self.quantity * self.price


class Order():
    def __init__(self, customer: customer, cart: List[Goods], prom=None) -> None:
        self.customer = customer
        self.cart = cart
        self.prom = prom

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(i.total() for i in self.cart)
        return self.__total

    def due(self):
        if self.prom is None:
            discount = 0
        else:
            discount = self.prom.discount(self)
        return self.total() - discount

    def __repr__(self) -> str:
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


class Prom(ABC):
    @abstractmethod
    def discount(self,order) -> float:
        '''discount'''

class discount1(Prom):
    def discount(self,order) -> float:
       return order.total() * 0.05 if order.customer.points >= 10000 else 0 

john = customer(name='vllbc', points=100000)
carts = [Goods(name='apple', quantity=5, price=10), Goods(
    name='banana', quantity=8, price=5), Goods(name='peach', quantity=4, price=8)]
order = Order(customer=john, cart=carts,prom=discount1())

print(order.total())
print(order)
