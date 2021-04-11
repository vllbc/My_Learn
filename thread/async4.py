import asyncio
import time
start = time.time()


async def job(t):
    start = time.time()
    print("start job")
    await asyncio.sleep(t)
    print(f"end job it takes {time.time() - start:.4f}s")

async def main():
    tasks = [asyncio.create_task(job(t)) for t in range(1,3)]
    await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(f"all works end for {time.time() - start:.4f}s")