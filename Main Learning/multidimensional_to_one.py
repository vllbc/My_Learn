from itertools import chain

lists = [[1,2,3],[4,5],[6]]
print(sum(lists,[]))
print([i for j in lists for i in j])
print(list(chain(*lists)))
from typing import Iterable
def flatten(items,ignore=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore):
            yield from flatten(x)
        else:
            yield x
print(list(flatten(lists)))