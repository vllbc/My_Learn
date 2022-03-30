from pydantic import BaseModel, conint, ValidationError 
from typing import (
    List, 
    Union,
    Optional,
    Dict
)

class Test(BaseModel):
    name: Optional[str]
    sex: Union[str, List[str]]
    d: Dict[str, int]
    id: conint(ge=1,le=10)
try:
    test = Test(name='wlb', sex='male', d={'dict':1}, id=1)
    print(test.dict(), test.__annotations__)
except ValidationError:
    print("数据错误")