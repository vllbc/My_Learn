from collections import namedtuple

test = namedtuple("test",['name','sex','age'])

t = test(name='wlb',sex='male',age=19)

print(t.name)