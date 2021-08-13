# 导入库
import requests
import csv
from lxml import etree


# 文件名
file_name = 'datas.csv'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
#开始的页数
start_page = 0
# 要爬取的页数
end_page = 260
# 构造urls
urls = [
    f'https://book.douban.com/tag/%E4%BA%A4%E4%BA%92%E8%AE%BE%E8%AE%A1?start={i}&type=T' for i in range(start_page, end_page+1, 20)]
    
# csv文件配置
fp = open(file_name, 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('标题', '作者', '译者', '出版社', '价格', '评分', '简介', '详细链接'))

# 获取数据并保存到文件

def get_urls_book(u):
    global authors, price, press
    res = requests.get(u, headers=headers)
    sele = etree.HTML(res.text)
    lis = sele.xpath(r'//*[@id="subject_list"]/ul/li')
    for li in lis:
        book_url = li.xpath('div[2]/h2/a/@href')[0]  # 书本的具体信息地址
        title = li.xpath('div[2]/h2/a/text()')[0].strip()  # 书的标题
        datas = li.xpath('div[2]/div[1]/text()')[0].strip("\n")  # 书的多种数据
        datas = datas.split('/')
        translator = ""  # 有的书有译者，有的书没有译者
        if len(datas) == 5:  # 有译者
            authors = datas[0].strip()
            translator = datas[1].strip()
            press = datas[2].strip()
            price = datas[4].strip()
        elif len(datas) == 4:  # 无译者
            authors = datas[0].strip()
            press = datas[1].strip()
            price = datas[3].strip()
        try:
            score = li.xpath('div[2]/div[2]/span[2]/text()')[0].strip()  # 书的评分
        except IndexError:  # 如果发生索引错误，说明评价人数少于10人
            score = "评价人数少于10人"
        try:
            introduction = li.xpath('div[2]/p/text()')[0].strip()  # 书的简介
        except IndexError:  # 如果发生索引错误，说明没有简介。
            introduction = "暂无简介"
        if translator != "":  # 有译者
            writer.writerow((title, authors, translator, press,
                             price, score, introduction, book_url))
        elif translator == "":  # 没有译者
            writer.writerow((title, authors, " ", press,
                             price, score, introduction, book_url))


# 主函数
if __name__ == '__main__':
    for url in urls:
        get_urls_book(url)
        print("完成-----------------")
    print("所有工作已完成！")  # 结束
