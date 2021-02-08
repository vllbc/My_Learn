import asyncio

async def test():
    await asyncio.sleep(3600)

async def run():
    try:
        await asyncio.wait_for(test(),1)
    except asyncio.TimeoutError:
        print("time out!")


asyncio.run(run())