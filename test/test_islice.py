from itertools import islice


def test():
    t = 0
    while True:
        yield t
        t += 1
        
for i in islice(test(), 10, 21, 2):
    print(i)
