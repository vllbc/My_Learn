def re_jie(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    else:
        return n*re_jie(n-1)
def re_sum(n):
    sum=0
    for i in range(0,n+1):
        sum+=re_jie(i)
    return sum
nums = []
for i in range(0,51):
    nums.append(re_sum(i))
    
print(list(map(str,nums)))
