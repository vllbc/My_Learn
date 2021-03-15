funcs = []
res = []
for x in range(7):
    def func(x=x):
        return x
    funcs.append(func)
    res.append(func())

func_res = [f() for f in funcs]

def create_mult():
    res = []
    for i in range(5):
        def func(x, i=i):
            return x * i
        res.append(func)
    return res
for cr in create_mult():
    print(cr(2))
