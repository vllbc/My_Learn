import asyncio
import random


# potato类
class Potato:
    # 生成土豆
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos
 
all_potatos = Potato.make(5)

## 这是一个异步生成器，可以用async for迭代
async def take_photos(nums):
    count = 0
    while True:
        # 如果没有土豆了，挂起请求生成土豆任务。
        if len(all_potatos) == 0:
            await askfor_photos()
        else:
            photo = all_potatos.pop()
            yield photo
            count += 1
            if count == nums :
                break

import time
async def askfor_photos():
    await asyncio.sleep(2)
    all_potatos.extend(Potato.make(5))

async def buy_photos():
    bucket = []
    async for p in take_photos(50):
        bucket.append(p)
        print(f"Go photo {id(p)}")

loop = asyncio.get_event_loop()
loop.run_until_complete(buy_photos())

