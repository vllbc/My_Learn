import threading
import time

exitflag = 0

class mythread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始进程"+self.name)
        print_time(self.name,self.counter,5)
        print("结束进程"+self.name)
    
def print_time(threadname,delay,counter):
        while counter:
            if exitflag:
                threadname.exit()
            time.sleep(delay)
            print("{} {}".format(threadname,time.ctime(time.time())))
            counter -= 1
thread1 = mythread(1,"thread1",1)
thread2 = mythread(2,"thread2",2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("exit")
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

