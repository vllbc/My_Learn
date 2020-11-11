# #docorator learning
# #-----------------------
# def logging(level):
#     def wapper(func):
#         def inner_wapper(*args, **wbargs):
#             print('{}  enter in{}()'.format(level, func.__name__))
#             return func(*args, **wbargs)
#         return inner_wapper
#     return wapper
# @logging('inner')
# def say(a):
#     print('wpcapp{}'.format(a))
# say('wlb')
#-----------------------
#-----------------------
import time
def print_time(func):
    def wapper(*args,**wbargs):
        print('{}()调用于{}'.format(func.__name__,time.time()))
        return func(*args,**wbargs)
    return wapper
@print_time
def my_name(aaa):
    print('look!{}'.format(aaa))
my_name("aaa")



        


# def dec(func):
#     print('call dec')
#     def indec(*args):
#         if len(args) == 0:
#             return 0
#         for m in args:
#             if not isinstance(m,int):
#                 return 0#如果实参不是整数，则直接返回0
#         return func(*args)
#     return indec
# @dec
# def my_sum(*args):
#     print('in mysum')
#     return sum(args)
# print(my_sum(1,2,3,4,5))

# @dec
# def pingjun(*ints):
#     print('in pingjun')
#     return sum(ints)/len(ints)
# print(pingjun(1,2,3,4,5))#3.0
# print(pingjun())#0
# print(pingjun)
# print(type(pingjun))
# print(type(pingjun()))