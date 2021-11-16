def partial(func,*wargs):
    def wapper(*kargs):
        args = list(wargs)
        print(f"args:{args}")
        print(f"kargs:{kargs}")
        args.extend(kargs)
        print(args)
        return func(*args)
    return wapper
def test(x,y):
    return x+y

T = partial(test,1)
print(T(2))