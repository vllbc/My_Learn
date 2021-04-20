def test():
    x = 0
    def inner(a):
        nonlocal x
        x = x + a
        return x
    return inner
t = test()
print(t(3))
print(t(3))
print(t(3))