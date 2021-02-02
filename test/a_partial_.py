def partial(func,*wargs):
    def wapper(*kargs):
        args = list(wargs)
        print(f"args:{args}")
        print(f"kargs:{kargs}")
        args.extend(wargs)
        return func(*args)
    return wapper