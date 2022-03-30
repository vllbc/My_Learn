import requests
import time
from pydantic import AnyHttpUrl


class FansSpider():
    def __init__(self, time: time.time()=5, start_fans: int=0, user_id=777536) -> None:
        self.api_url: AnyHttpUrl = f"https://api.bilibili.com/x/relation/stat?vmid={user_id}&jsonp=jsonp"
        self.time: time.time() = time
        self.fans: int = start_fans

    @classmethod
    def get_fans(cls) -> int:
        return requests.get(cls().api_url).json()['data']['follower']

    @classmethod
    def initfans(cls,time=5, user_id=777536) -> "FansSpider":
        return cls(time=time, start_fans=cls.get_fans(), user_id=user_id)

    def __str__(self) -> str:
        return str(self.fans)
    
    def get_fans_change(self) -> int:
        news = FansSpider.get_fans()
        changes = news - self.fans
        self.fans = news
        return changes 
    
    def update_fans(self) -> None:
        self.fans = FansSpider.get_fans()

    __repr__ = __str__


f = FansSpider.initfans(time=5)
print(f"开始当前粉丝数为{f}")
time.sleep(f.time)

while True:
    print(f"当前粉丝数{f} {f.time}s内粉丝变化为{f.get_fans_change()}")
    time.sleep(f.time)
