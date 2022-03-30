urls = ['https://www.qidian.com/rank/collect?page={}'.format(i) for i in range(1, 6)]

args = {
    'sex': 'GG',
    'year': '2021'
}
def add_url(year):
    def wapper(url):
        return f'{url}&year={year}'
    return wapper

print(list(map(add_url(args['year']), urls)))