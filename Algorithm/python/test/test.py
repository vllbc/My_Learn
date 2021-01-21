def max_yue(a,b):
    return a if b == 0 else max_yue(b,a%b)
try:
    n = int(input())
    nums = list(map(int,input().split()))
    y = max_yue(nums[0],nums[1])
    print("{}/{}".format(nums[0]//y,nums[1]//y))
except:
    print(0)