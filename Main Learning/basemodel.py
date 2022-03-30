from pydantic import BaseModel,AnyUrl


class Test(BaseModel): # 继承后可以用类属性创建实例
    url: AnyUrl
    data: str

    def __str__(self):
        return self.url + self.data
    

kwargs = {
    'url': 'https://www.baidu.com',
    'data': '/search'
}
print(Test(**kwargs))