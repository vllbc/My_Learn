import requests
from lxml import etree
import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='xwh5201314',db='spider',port=3306,charset='utf8')
cur = conn.cursor()

urls = ['https://www.qidian.com/rank/collect?page={}'.format(i) for i in range(1,6)]
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
def insert_data(url):
    res = requests.get(url,headers=header)
    sel = etree.HTML(res.text)
    infos = sel.xpath('//*[@id="rank-view-list"]/div/ul/li')
    for info in infos:
        titles = info.xpath('div[2]/h4/a/text()')[0]
        authors = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        classess = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        cur.execute("insert into qidian (title,author,classes) values('{}','{}','{}');".format(str(titles),str(authors),str(classess)))
for url in urls:
    print("Start---")
    insert_data(url)
    print("one OK")
conn.commit()



