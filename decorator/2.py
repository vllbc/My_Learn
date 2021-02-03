import time
import logging

logging.basicConfig(level = logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("start debug")
def display_time(func):
    def wrp(*args):
        t1 = time.time()
        res = func(*args)
        t2 = time.time()
        print("total time is {:.4}".format(t2-t1))
        print(f"result = {res}") #将结果在这里输出
    return wrp
def is_zhishu(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i==0:
                return False

        return True

@display_time

def mainfunc(maxnum):
    count = 0
    for i in range(1,maxnum):
        if is_zhishu(i):
            count += 1
            logging.debug(f"count = {count}")
    return count
mainfunc(100)
logging.debug("end debug")