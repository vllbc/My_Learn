funcs = []
res = []
for x in range(7):
    def func(x=x): # 去掉x=x则出现[6,6,6,6,6,6] 在循环内部定义一个函数时, 如果该函数在其主体中使用了循环变量, 则闭包函数将与循环变量绑定, 而不是它的值. 因此, 所有的函数都是使用最后分配给变量的值来进行计算的.
        return x
    funcs.append(func)
    res.append(func())

func_res = [f() for f in funcs]
print(func_res)
def create_mult():
    res = []
    for i in range(5):
        def func(x, i=i): # 去掉i=i则全输出8，原因和上面一样
            return x * i
        res.append(func)
    return res
for cr in create_mult():
    print(cr(2))
