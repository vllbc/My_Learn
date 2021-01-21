import asyncio
import random


class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos
    
all_potatos = Potato.make(5)

async def take_photos(nums):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await askfor_photos()
        else:
            photo = all_potatos.pop()
            yield photo
            count += 1
            if count == nums :
                break


async def askfor_photos():
    await asyncio.sleep(2)
    all_potatos.append(Potato.make(5))

async def buy_photos():
    bucket = []
    async for p in take_photos(50):
        bucket.append(p)
        print(f"Go photo {id(p)}")

loop = asyncio.get_event_loop()
loop.run_until_complete(buy_photos())

