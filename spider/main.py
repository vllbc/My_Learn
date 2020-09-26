import requests
from lxml import etree

urls = ["https://www.tupianzj.com/meinv/20160215/40823_{}.html".format(num) for num in range(2,10)]
header ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
def paqu(url,name):
    res = requests.get(url)
    sele = etree.HTML(res.text)
    photo_url = sele.xpath('//*[@id="bigpicimg"]/@src')[0]
    data = requests.get(photo_url)
    fb = open(r'C:\\Users\\vllbc\Desktop\\妹子图\\{}.jpg'.format(name),'wb')
    fb.write(data.content)
    fb.close()
num = 1
for url in urls:
    
    paqu(url,num)
    num += 1