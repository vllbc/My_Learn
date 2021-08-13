import requests
from lxml import etree
import re

# 构造五页
urls = [f"https://www.photocome.com/search?q=%E9%A3%8E%E6%99%AF&page={n}" for n in range(1,6)]

# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

# 保存图片
def save_pic(pic_url,pic_name):
    with open(f"pic/{pic_name}.jpg",'wb') as fp:
        content = requests.get(pic_url).content
        fp.write(content)

# 爬取图片路径
def spider(url):
    res = requests.get(url, headers=headers).text
    sele = etree.HTML(res)
    selectors = sele.xpath('//*[@class="_2gLVL _33Mfr"]')
    pic_urls = list()
    for selector in selectors:
        pic_urls.append(selector.xpath("a/img/@src")[0])
    for pic_url in pic_urls:
        save_pic("https:"+pic_url,pic_url[-11:-4])

for url in urls:
    spider(url)