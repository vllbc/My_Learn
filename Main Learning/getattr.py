class Test:
    x = 1
    def __init__(self):
        self.y = 2
    def __getattr__(self, name):
        return name
print(getattr(Test(), 'mofa')) # == Test().mofa
print(Test().mofa)
print(getattr(Test, 'x')) # == Test.x
print(getattr(Test(), 'y')) # == Test().y
<<<<<<< HEAD
print(getattr(Test(), 'x'))
=======
>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf
# getattr()主要用于获取对象的属性，如果属性不存在，则返回None,也可以设置默认值,default参数。