from functools import partial

def digits_(file,block_size=1024*8):
    _read = partial(file.read,block_size)
    for line in iter(_read,""):
        for s in line:
            if s.isdigit():
                yield s

def count_digits(fname):
    """计算文件里包含多少个数字字符"""
    count = 0
    block_size = 1024*8
    with open(fname) as file:
        for _ in digits_(file=file):
            count+=1
    return count
print(count_digits("testvim.txt"))