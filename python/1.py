#  '''import os 
#  print(os.getcwd())'''读取当前路径 根据当前路径读取文件
# conturies = []
# file = open("remain-python\\countries_zh.csv","r",encoding="utf-8")
# for fi in file:
#     fi = fi.strip()
#     arr = fi.split(",")
#     a = arr[1]
#     b = arr[3]
#     c = int(arr[4])#注意要换成整数型
#     conturies.append((a,b,c))
    
# conturies.sort(key=lambda cou:cou[2])
# for contury in conturies:
#     print(contury)
def fun(a,b,c):
    return lambda x:a*x^2+b*x+c

   
print(fun(1,2,3)(888))