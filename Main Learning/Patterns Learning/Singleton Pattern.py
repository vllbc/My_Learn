from typing import Any


class JustHaveInstance(Exception):
    pass

class Test:
    __instance = None
    __already_have = False
    def __new__(cls) -> Any:
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__already_have:
            print("创建成功")
            Test.__already_have = True
        else:
            raise JustHaveInstance()
        
t = Test()

t2 = Test()