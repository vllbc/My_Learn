def honer(n,A,B,C):#A为初始位置，B为通过的位置，C为最终位置
    if n == 1:
        print('{}>>>>{}'.format(A,C))#递归出口
    else:
        honer(n-1,A,C,B)#将A上的通过C移动到B
        print('{}>>>>{}'.format(A,C))
        honer(n-1,B,A,C)#将B上的通过A移动到C

honer(6,'A','B','C')
