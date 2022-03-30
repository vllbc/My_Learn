nums = []
for i in range(100000001,1000000001):
    if i==int(''.join(reversed(str(i)))):
        nums.append(i)
def is_zhi(n):
    if n==1:
        return False
    for i in range(2,(int(n**(1/2)))+1):
        if n%i==0:
            return False
    return True
numss=[]
for i in nums:
    if is_zhi(i):
        numss.append(i)
print(numss)