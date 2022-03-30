import requests
from lxml import etree
import csv


f = open("小火花数据中心.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(("头条号", "粉丝数", "阅读数", "评论数", "发文数"))


class Spider:
    def __init__(self):
        self.url = "https://baowen.xhh.com/charts"

    def get_all_datas(self):
        res = requests.get(self.url).text
        select = etree.HTML(res)
        return select.xpath("/html/body/section[2]/div/div/table/tbody/tr")

    def get_and_save(self, selector):
        name = selector.xpath("td[2]/a/text()")[0]
        fans = selector.xpath("td[3]/text()")[0]
        readings = selector.xpath("td[4]/text()")[0]
        comments = selector.xpath("td[5]/text()")[0]
        publish = selector.xpath("td[6]/text()")[0]
        writer.writerow((name, fans, readings, comments, publish))

    def run(self):
        for i in self.get_all_datas():
            self.get_and_save(i)


Spider().run()
