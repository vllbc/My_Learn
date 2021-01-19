# alps = 'abcdefghijklmnopqrstuvwxyz'
# def transf(c):
#     if c.isalpha():
#         idx = (alps.index(c)+2) % 26
#         return alps[idx]
#     else:
#         return c
# text = "map"
# res = ''
# for i in text:
#     res += transf(i)
# print(res)
# def partial(func,*wargs):
#     def wapper(*kargs):
#         args = list(wargs)
#         print(f"args:{args}")
#         print(f"kargs:{kargs}")
#         args.extend(wargs)
#         return func(*args)
#     return wapper


# from functools import wraps

# def out_wapper(*wargs):
#     def partial(func):
#         @wraps(func)
#         def wrapper(*kargs):
#             args = list(wargs)
#             print(f"args:{args}")
#             print(f"kargs:{kargs}")
#             args.extend(kargs)
#             print(f"last:{args}")
#             return func(*args)
#         return wrapper
#     return partial

# @out_wapper(1,2)
# def add(a,b,c):
#     return a + b + c

# print(add(3))




# class A:
    # bar = 1
    # def func1(self):  
        # print ('foo') 
    # @classmethod
    # def func2(cls):
        # print ('func2')
        # print (cls.bar)
        # cls().func1()   # 调用 foo 方法
#  
# A.func2()               # 不需要实例化


# class A(object):
    
#     # 属性默认为类属性（可以给直接被类本身调用）
#     num = "类属性"

#     # 实例化方法（必须实例化类之后才能被调用）
#     def func1(self): # self : 表示实例化类后的地址id
#         print("func1")
#         print(self)

#     # 类方法（不需要实例化类就可以被类本身调用）
#     @classmethod
#     def func2(cls):  # cls : 表示没用被实例化的类本身
#         print("func2")
#         print(cls)
#         print(cls.num)
#         cls().func1()

#     # 不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
#     def func3():
#         print("func3")
#         print(A.num) # 属性是可以直接用类本身调用的
    
# # A.func1() 这样调用是会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
# A.func2()
# A.func3() 




# import time
# import functools

# class DelayFunc:
#     def __init__(self,  duration, func):
#         self.duration = duration
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         print(f'Wait for {self.duration} seconds...')
#         time.sleep(self.duration)
#         return self.func(*args, **kwargs)

#     def eager_call(self, *args, **kwargs):
#         print('Call without delay')
#         return self.func(*args, **kwargs)


# def delay(duration):
#     def partial(func):
#         return DelayFunc(duration,func)
#     return partial

# @delay(2)
# def add(a,b):
#     print(a+b)
# add.eager_call(1,2)


# class Test:
#     count = 0
#     def __init__(self):
#         Test.count += 1

# Test()
# Test()
# print(Test.count)


# class Chain(object):
    
#     def __init__(self, path=''):
#         self._path = path

#     def __getattr__(self, path):

#         return Chain('%s/%s' % (self._path, path))

#     def __str__(self):
#         return self._path
    
#     def users(self,name):
#         return Chain(f"{self._path}/users/{name}")

#     __repr__ = __str__



# class Field(object):
    
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type

#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)

# class StringField(Field):
#     def __init__(self, name, column_type='TXT'):
#         super().__init__(name, column_type)


# class IntegerField(Field):
#     def __init__(self, name, column_type='INT'):
#         super().__init__(name, column_type)


# class ModelMetaclass(type):

#     def __new__(cls,name,bases,attrs):
#         if name == 'Model':
#             return type.__new__(cls,name,bases,attrs)
#         print(f"found model {name}")
#         maps = dict()
#         for k,v in attrs.items():
#             if isinstance(v,Field):
#                 print(f"Found mapping {k} ==> {v}")
#                 maps[k] = v
#         for k,v in maps.items():
#             attrs.pop(k)
#         attrs['__mappings__'] = maps
#         attrs['__table__'] = name
#         return type.__new__(cls,name,bases,attrs)


# class Model(dict, metaclass=ModelMetaclass):
    
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)

#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)

#     def __setattr__(self, key, value):
#         self[key] = value

#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(k)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))


# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')

# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()



test = "智科20-1-1-213--31—光电－"
import re
print(re.sub(r"[\d*\-*\—*\－*]","",test))