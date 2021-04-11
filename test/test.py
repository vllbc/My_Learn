import pickle

d = dict(name='name',sex='male')
f = open("test.pkl",mode='wb')
pickle.dump(d,f)
f.close()
with open("test.pkl",mode='rb') as fp:
    d = pickle.load(fp)
    print(d)