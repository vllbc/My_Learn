import random
import wrapt # 为第三方库

def provide_number(min_num, max_num):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        # 参数含义：
        #
        # - wrapped：被装饰的函数或类方法
        # - instance：
        #   - 如果被装饰者为普通类方法，该值为类实例
        #   - 如果被装饰者为 classmethod 类方法，该值为类
        #   - 如果被装饰者为类/函数/静态方法，该值为 None
        #
        # - args：调用时的位置参数（注意没有 * 符号）
        # - kwargs：调用时的关键字参数（注意没有 ** 符号）
        #
        num = random.randint(min_num, max_num)
        # 无需关注 wrapped 是类方法或普通函数，直接在头部追加参数
        args = (num,) + args
        return wrapped(*args, **kwargs)
    return wrapper
    


@provide_number(1, 100)
def print_random_number(num):
    print(num)
    
class Foo:
    @provide_number(1, 100)
    def print_random_number(self, num):
        print(num)

# 输出 1-100 的随机整数
# OUTPUT: 72
Foo().print_random_number()
print_random_number()

# 使用 wrapt 模块编写的装饰器，相比原来拥有下面这些优势：

# 嵌套层级少：使用 @wrapt.decorator 可以将两层嵌套减少为一层
# 更简单：处理位置与关键字参数时，可以忽略类实例等特殊情况
# 更灵活：针对 instance 值进行条件判断后，更容易让装饰器变得通用