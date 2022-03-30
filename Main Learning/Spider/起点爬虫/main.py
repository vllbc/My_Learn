import queue
import requests
from lxml import etree
import time
import csv

fp = open("res.csv", "w+", newline="")
writer = csv.writer(fp)
writer.writerow(("title", "author", "classes"))
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

urls = [
    'https://www.qidian.com/rank/collect?page={}'.format(i) for i in range(1, 6)]

def spider(url):
    res = requests.get(url, headers=headers).text
    sel = etree.HTML(res)
    infos = sel.xpath('//*[@id="book-img-text"]/ul/li')
    for info in infos:
        title = info.xpath('div[2]/h2/a/text()')[0]
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]   
        classes = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        writer.writerow((title, author, classes))


for url in urls:
    spider(url)
fp.close()
