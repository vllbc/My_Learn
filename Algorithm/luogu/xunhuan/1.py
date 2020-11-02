def re_jie(n):
    if n==1:
        return 1
    else:
        return n*re_jie(n-1)

def re_sum(m):
    sum=0
    for i in range(1,m+1):
        sum+=re_jie(i)
    return sum
for a in range(1,51):
    print('"{}",'.format(re_sum(a)))
