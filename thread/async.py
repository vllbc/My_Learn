import asyncio,aiohttp,time


async def dosomething(n):
    await asyncio.sleep(n)
    print(f"done  {dosomething.__name__}")


loop = asyncio.get_event_loop()
start = time.time()
tasks = []
for i in range(10):
    coroutine = dosomething(1)
    task = loop.create_task(coroutine)
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f"耗时{end-start:.4f}")