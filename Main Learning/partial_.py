# def partial(func,*wargs):
#     def wapper(*kargs):
#         args = list(wargs)
#         print(f"args:{args}")
#         print(f"kargs:{kargs}")
#         args.extend(kargs)
#         print(args)
#         return func(*args)
#     return wapper
# def test(x,y):
#     return x+y

# T = partial(test,1)
# print(T(2))
from functools import wraps,partial

def out_wapper(*wargs):
    def partialout(func):
        return partial(func,*wargs)
        # @wraps(func)
        # def wrapper(*kargs):
        #     args = list(wargs)
        #     print(f"args:{args}")
        #     print(f"kargs:{kargs}")
        #     args.extend(kargs)
        #     print(f"last:{args}")
        #     return func(*args)
        # return wrapper
    return partialout
#这个是装饰器版本的
@out_wapper(1,2)
def add(a,b,c):
    return a + b + c

print(add(3)) #输出和上面一样
#明显装饰器要麻烦一点实现，不过毕竟是封装好的函数，以后直接用就可以，不过了解这些有助于提高思维水平