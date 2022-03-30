from io import StringIO,BytesIO

s = StringIO("")
s.write("hello")
print(s.getvalue())
s.seek(0)
print(s.readline())

import pickle
def f(**kwargs):
    print(kwargs)


d = dict(name="wlb", sex='male')
p = pickle.dumps(d)
with open('test_pickle.txt', 'rb') as fp:
    print(pickle.loads(fp.read()))
