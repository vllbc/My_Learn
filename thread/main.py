import threading
import time
event = threading.Event()
def lighter():
    count = 0
    event.set()     #初始值为绿灯
    while True:
        if 5 < count <=10 :
            event.clear()  # 红灯，清除标志位
            print("\33[41;1mred light is on...\033[0m")
        elif count > 10:
            event.set()  # 绿灯，设置标志位
            count = 0
        else:
            print("\33[42;1mgreen light is on...\033[0m")

        time.sleep(1)
        count += 1
def car(name):
    while True:
        if event.is_set():      #判断是否设置了标志位
            print("[%s] running..."%name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..."%name)
            event.wait(1)
            print("[%s] green light is on,start going..."%name)
light = threading.Thread(target=lighter,)
light.start()
car = threading.Thread(target=car,args=("MINI",))
car.start()




# import threading
# import queue,time
# class threads(threading.Thread):
#     def __init__(self,func,*args):
#         super().__init__()
#         self.func = func
#         self.arg = args
#     def run(self):
#         self.func(''.join(self.arg))

# q=queue.Queue(maxsize=10)
# def Producer(name):
#     count=1
#     while True:
#         q.put("骨头 %s"%count)
#         print("{}生产了骨头".format(name),count)
#         count+=1
#         time.sleep(1)      
# def Consumer(name):
#     while True:
#         print("[%s] 取到  [%s] 并且吃了它。。。"%(name,q.get()))
#         time.sleep(1)
# p = threads(Producer,'wlb')
# c = threads(Consumer,'yyh')
# c1 = threads(Consumer,'zwh')
# # p=threading.Thread(target=Producer,args=('wlb',))
# # c=threading.Thread(target=Consumer,args=("yangyuhao",))
# # c1=threading.Thread(target=Consumer,args=("zhangwenhao",))
# p.start()
# c.start()
# c1.start()