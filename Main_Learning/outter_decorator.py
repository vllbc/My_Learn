
from functools import wraps


def out_wapper(*wargs):
    def partial(func):
        @wraps(func)
        def wrapper(*kargs):
            args = list(wargs)
            print(f"args:{args}")
            print(f"kargs:{kargs}")
            args.extend(kargs)
            print(f"last:{args}")
            return func(*args)
        return wrapper
    return partial


@out_wapper(1, 2)
def add(a, b, c):
    return a + b + c


print(add(3))
