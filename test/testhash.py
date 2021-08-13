from collections import namedtuple

test = namedtuple("test",["name","age"])

dic = {
    "name":"wlb",
    "age":18
}
wlb = test(**dic)
a,b = wlb
print(a,b)