num1 = input("")
if int(num1)>=0:#如果是非负数
    num2 = num1[::-1]#反转字符串
    res = int(num2.lstrip("0"))#去除首位的0
else:
    res = -int(num1[1:][::-1].lstrip("0"))
print(res)