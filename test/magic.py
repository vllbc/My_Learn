class Chain(object):
    
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):

        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    
    def users(self,name):
        return Chain(f"{self._path}/users/{name}")

    __repr__ = __str__

chain = Chain("vllbc")
print(chain.a.a.a.a.a)