def simple_coro2(a):
    print('-> Started: a = ', a)
    b = yield a
    print('-> Received b = ', b)
    c = yield a + b
    print('-> Received c = ', c)

coro2 = simple_coro2(11)
print(next(coro2)) # 预缴携程 在yield处暂停，才能使用send
print(coro2.send(22))
print(coro2.send(33))