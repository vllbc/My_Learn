<<<<<<< HEAD

=======
import queue
>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf
import requests
from lxml import etree
import pymysql
import logging
from threading import Thread,Lock
from queue import Queue
import time


# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# logger = logging.getLogger('qidian')

# class Qidian_Spider:
#     def __init__(self):
#         self.conn,self.cur = self.connet_mysql()
#         self.urls = self.create_urls()
#         self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
#     def connet_mysql(self):
#         conn = pymysql.connect(host='localhost',user='root',passwd='',db='spider',port=3306,charset='utf8')
#         cur = conn.cursor()
#         return conn,cur
#     def create_urls(self):
#         urls = ['https://www.qidian.com/rank/collect?page={}'.format(i) for i in range(1,6)]
#         return urls
#     def insert_data1(self,url):
#         self.conn,self.cur = self.connet_mysql()
#         res = requests.get(url,headers=self.headers)
#         sel = etree.HTML(res.text)
#         infos = sel.xpath('//*[@id="rank-view-list"]/div/ul/li')
#         titles = []
#         authors = []
#         classess = []
#         for info in infos:
#             title = info.xpath('div[2]/h4/a/text()')[0]
#             author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
#             classes = info.xpath('div[2]/p[1]/a[2]/text()')[0]
            
#             self.cur.execute("insert into qidian (title,author,classes) values('{}','{}','{}');".format(str(title),str(author),str(classes)))
#             # logger.info("---ok")
#         self.conn.commit()
#     def insert_data(self,url):
#         self.conn,self.cur = self.connet_mysql()
#         # logger.info("start")
#         res = requests.get(url,headers=self.headers)
#         sel = etree.HTML(res.text)
#         infos = sel.xpath('//*[@id="rank-view-list"]/div/ul/li')
#         titles = []
#         authors = []
#         classess = []
#         for info in infos:
#             title = info.xpath('div[2]/h4/a/text()')[0]
#             author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
#             classes = info.xpath('div[2]/p[1]/a[2]/text()')[0]
            
#             self.cur.execute("insert into qidian (title,author,classes) values('{}','{}','{}');".format(str(title),str(author),str(classes)))
#             # logger.info("---ok")
#         self.conn.commit()
#     def run(self):
#         print("正常程序开始")
#         for url in self.urls:
#             # logger.info("Start---")
#             self.insert_data1(url)
#             # logger.info("one OK")
#         self.cur.close()
# mains = Qidian_Spider()
# start = time.time()
# mains.run()
# print(f"正常耗时{time.time()-start:.4f}s")

conn = pymysql.connect(host='localhost',user='root',passwd='',db='spider',port=3306,charset='utf8')
cur = conn.cursor()
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
lock = Lock()
print('多线程开始')
def duo_spider(queues):
    while queues.empty() is not True:
        res = requests.get(queues.get(),headers=headers)
        sel = etree.HTML(res.text)
        infos = sel.xpath('//*[@id="rank-view-list"]/div/ul/li')
        for info in infos:
            title = info.xpath('div[2]/h4/a/text()')[0]
            author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
            classes = info.xpath('div[2]/p[1]/a[2]/text()')[0]
            lock.acquire() # 要加上一个互斥锁，因为多个线程共同修改同一个数据库，不加锁会引发错误。这一点也要注意，不加锁的话，如果线程数量多了，就会出现数据库插入数据的顺序不对的情况。
            cur.execute("insert into qidian (title,author,classes) values('{}','{}','{}');".format(str(title),str(author),str(classes)))
            conn.commit()
            lock.release()
        queues.task_done() #!! 注意的是，要在结束后运行queues.task_done()不然会引发数据库错误
        
urls = ['https://www.qidian.com/rank/collect?page={}'.format(i) for i in range(1,6)]
start = time.time()
in_q = Queue()
for u in urls:
    in_q.put(u)
for _ in range(10):
    thread = Thread(target=duo_spider,args=(in_q,))
    thread.daemon = True
    thread.start()
in_q.join()
print(f"多线程耗时{time.time()-start:.4f}s")


