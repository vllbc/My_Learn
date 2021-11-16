import requests
from lxml import etree
import csv

url = "https://web.phb123.com/renwu/fuhao/px_CN.html"

fp = open("res.csv", "wt", newline="", encoding="utf-8")
writer = csv.writer(fp)
writer.writerow(("中国排名", "世界排名", "名字", "财富值"))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}


def get_loop():
    res = requests.get(url, headers=headers).text
    selector = etree.HTML(res)
    loops = selector.xpath('/html/body/div[4]/table/tbody/tr')
    return loops


def main():
    for loop in get_loop()[1:101]:
        China_rank = loop.xpath('td[1]/text()')[0]
        world_rank = loop.xpath('td[2]/text()')[0]
        try:
            name = loop.xpath('td[3]/text()')[0]
        except IndexError:
            name = ""
        money = loop.xpath('td[4]/text()')[0]
        writer.writerow((China_rank, world_rank, name, money))


main()
fp.close()
