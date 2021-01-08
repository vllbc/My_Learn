import requests
import csv
from lxml import etree

file_name = 'datas.csv'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
urls = [f'https://book.douban.com/tag/%E4%BA%A4%E4%BA%92%E8%AE%BE%E8%AE%A1?start={i}&type=T' for i in range(0, 261, 20)]
# 构造urls
fp = open(file_name, 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('标题', '作者', '译者', '出版社', '价格', '评分', '简介', '详细链接'))


def get_urls_book(u):
    global zuozhes, jiaqian, chubanshe
    res = requests.get(u, headers=headers)
    sele = etree.HTML(res.text)
    lis = sele.xpath(r'//*[@id="subject_list"]/ul/li')
    for li in lis:
        book_url = li.xpath('div[2]/h2/a/@href')[0]
        title = li.xpath('div[2]/h2/a/text()')[0].strip()
        datas = li.xpath('div[2]/div[1]/text()')[0].strip("\n")
        datas = datas.split('/')
        yizhe = ""
        if len(datas) == 5:
            zuozhes = datas[0].strip()
            yizhe = datas[1].strip()
            chubanshe = datas[2].strip()
            jiaqian = datas[4].strip()
        elif len(datas) == 4:
            zuozhes = datas[0].strip()
            chubanshe = datas[1].strip()
            jiaqian = datas[3].strip()
        try:
            pingfen = li.xpath('div[2]/div[2]/span[2]/text()')[0].strip()
            jianjie = li.xpath('div[2]/p/text()')[0].strip()
        except IndexError:
            pingfen = "评价人数少于10人"
            jianjie = "暂无简介"
        if yizhe != "":
            writer.writerow((title, zuozhes, yizhe, chubanshe, jiaqian, pingfen, jianjie, book_url))
        elif yizhe == "":
            writer.writerow((title, zuozhes, " ", chubanshe, jiaqian, pingfen, jianjie, book_url))


for url in urls:
    get_urls_book(url)
    print("完成-----------------")
