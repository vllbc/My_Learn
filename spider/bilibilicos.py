import requests
import json
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
urls = [f'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num={f}&page_size=20' for f in range(1,25)]
def get_photo(url):
    res = requests.get(url,headers=headers)
    jsons = json.loads(res.text)
    lists = jsons['data']['items'][0]['item']['pictures']
    url_list=[]
    for list in lists:
        url_list.append(list['img_src'])
    for urld in url_list:
        ress = requests.get(urld,headers=headers)
        fp = open(f'meizitu\\{urld[-20:]}','wb')
        fp.write(ress.content)
        fp.close()
for url in urls:
    get_photo(url)