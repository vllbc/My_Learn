#子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total/count
    return total,count,average
    
# 委托生成器
def proxy_gen():
    while True:
        total,count,average = yield from average_gen()
        print(total,count,average)

def main():
    t = proxy_gen()
    next(t)
    print(t.send(10))
    print(t.send(15))
    print(t.send(20))
    t.send(None)
main()
