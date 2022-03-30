import re

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

for i in re.finditer(re_telephone,"010-12345"):
    print(i.group(0))

A = re.findall(re_telephone,'010-12345')[0]
print(A)
B = re.findall(re_telephone,'010-2313')[0]
print(B)

text = '<div class="nam">中国</div>'
fin = re.findall('<div class=".*">(.*?)</div>',text)[0]
print(fin)    

        