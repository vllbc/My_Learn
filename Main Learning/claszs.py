from pydantic import BaseModel
from typing import Any


class cout():
    def __init__(self, cls: "Test", text: str) -> None: 
        self.cls = cls
        self.text = text
    
    def __str__(self) -> Any:
        return f"{self.cls}  {self.text}"

# 程序到cout时 Test类并没有定义，但最后Test在变量空间中，所以加上引号

class Test(BaseModel):
    def __str__(self) -> str:
        return "I am Test Class"


print(cout(cls=Test(), text="hello world!"))