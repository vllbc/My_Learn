def logging(level):
    def wapper(func):
        def inner_wapper(*args, **wbargs):
            print('{}  enter in{}()'.format(level, func.__name__))
            return func(*args, **wbargs)
        return inner_wapper
    return wapper
@logging('inner')
def say(a):
    print('wpcapp{}'.format(a))
say('wlb')
import time
def print_time(func):
    def wapper(*args,**wbargs):
        print('{}()调用于{}'.format(func.__name__,time.time()))
        return func(*args,**wbargs)
    return wapper
@print_time
def my_name(aaa):
    print('look!{}'.format(aaa))
def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print('pass')
        else:
            print('failed')
    return cmp
passline = set_passline(90)
passline(89)


def dec(func):
    print('call dec')
    def indec(*args):
        if len(args) == 0:
            return 0
        for m in args:
            if not isinstance(m,int):
                return 0
        return func(*args)
    return indec
@dec
def my_sum(*args):
    print('in mysum')
    print(sum(args))
my_sum(1,2,3,4,5)
import time
def pprint_time(func):
    def dec(*arg,**args):
        print('{}调用于{}'.format(func.__name__,time.time()))
        print(func(*arg,**args))
    return dec
@pprint_time
def han(xx):
    return '{}'.format(xx)
han('123')


def main(func):
    def com(*arg):
        if len(arg) == 0:
            return 0
        for i in arg:
            if not isinstance(i,int):
                return 0
        return func(*arg)
    return com

@main
def pingjun(*ints):
    return sum(ints)/len(ints)
print(pingjun(1,2,3,4,5))
print(pingjun())
print(pingjun)
print(type(pingjun))
print(type(pingjun()))