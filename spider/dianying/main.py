import requests
from lxml import etree
import json
from queue import Queue
import threading

urls = [f'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E8%A7%86%E5%89%A7&start={i}&genres=%E5%96%9C%E5%89%A7&qq-pf-to=pcqq.c2c' for i in range(420,2001,20)]
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
   'Cookie': '改成你自己账号的cookie 最好多弄几个账号 '
}
with open('host.txt','r') as fp:
    ips = fp.readlines()
    ips = [ip.strip() for ip in ips]


def get_datas_url(url,ids):
    proxies = {
        'http':'http://'+ips[ids]
    }
    res = requests.get(url,headers=headers,proxies=proxies)
    res = json.loads(res.text,strict=False)
    urls = []
    try:
        for data in res['data']:
            urls.append(data['url'])
    except KeyError:
        pass
    return urls
def get_datas(url):

    res = requests.get(url,headers=headers)
    sele = etree.HTML(res.text)
    title = sele.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
    daoyan = sele.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
    bianju = sele.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')
    zhuyan = sele.xpath('//*[@rel="v:starring"]/text()')
    classes = sele.xpath('//*[@property="v:genre"]/text()')
    datas = sele.xpath('//*[@id="info"]/text()')
    datas = ''.join(datas).strip().split()
    while '/' in datas:
        datas.remove('/')
    zhipiandiqu = datas[0]
    yuyan = datas[1]
    try:
        pingfen = sele.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0].strip()
        jianjie = sele.xpath('//*[@id="link-report"]/span/text()')[0].strip()
    except IndexError:
        pingfen = "暂无评分"
        jianjie = "暂无简介"
    try:
        with open(fr"data/{title}.txt",'a+',encoding='utf-8') as fp:
            fp.write(f'''名字:{title}
    导演:{'/'.join(daoyan)}
    编剧:{'/'.join(bianju)}
    主演:{'/'.join(zhuyan)}
    类别:{'/'.join(classes)}
    制片地区:{zhipiandiqu}
    语言:{yuyan}
    评分:{pingfen}
    简介:{jianjie}
                        ''')
            print("ok")
    except OSError as e:
        print(e)
    

for url in urls:
    n = 0
    try:
        page_urls = get_datas_url(url,n)
    except KeyError:
        n+=1
        page_urls = get_datas_url(url,n)
    for u in page_urls:
        get_datas(u)
    print("-------------------------")
