<<<<<<< HEAD
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
=======
import asyncio

async def test():
    await asyncio.sleep(3600)

async def run():
    try:
        await asyncio.wait_for(test(),1)
    except asyncio.TimeoutError:
        print("time out!")


asyncio.run(run())
>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf
