class Chain(object):
    
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __getitem__(self,path):
        if isinstance(path, slice):
            print("i am slice")
            return 1

    def __str__(self):
        return self._path
    
    def users(self,name):
        return Chain(f"{self._path}/users/{name}")

    __repr__ = __str__

chain = Chain("vllbc")
print(chain[1:2])
print(chain.x.x.x.x.x)