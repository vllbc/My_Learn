import asyncio
import time


async def say_after(name,wait):
    await asyncio.sleep(wait)
    print(name)
    return 1

def callback1(task):
    print("taks1完成", task._state)
async def main():
    print("Start!")
    task1 = asyncio.create_task(say_after('wlb',1))
    task2 = asyncio.create_task(say_after('yyh',2))
    task1.add_done_callback(callback1)
    start = time.time()
    res = await asyncio.gather(task1,task2) 
    end = time.time()
    print(f"耗时{end - start}")
    print(res)
    print("End!")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())