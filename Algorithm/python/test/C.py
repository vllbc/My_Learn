def max_yue(a,b):
    return a if b == 0 else max_yue(b,a%b)
def a_b(a,b):
    if a == b:
        return a
    if b < a:
        a,b = b,a
    return a_b(min(b//a,a),max(b//a,a))
try:
    n = int(input())
    fenzi,fenmu = [],[]
    nums = sorted(list(map(int,input().split())))
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            continue
        y = max_yue(nums[i],nums[i+1])
        fenzi.append(nums[i+1]//y)
        fenmu.append(nums[i]//y)
    fz,fm = fenzi[0],fenmu[0]
    for i in range(1,len(fenzi)):
        fz = a_b(fz,fenzi[i])
        fm = a_b(fm,fenmu[i])
    print("{}/{}".format(fz,fm))
except:
    print("0/0")
