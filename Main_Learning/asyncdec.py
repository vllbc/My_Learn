from functools import wraps
import asyncio

def decorator(func):
    @wraps(func)
    async def hello(*args, **kwargs):
        await asyncio.sleep(2)
        return await func(*args,**kwargs)
    return hello

@decorator
async def test():
    print("hello")
asyncio.run(test())