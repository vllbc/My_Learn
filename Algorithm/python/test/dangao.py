n,k = input().split()
k = int(k)
nums = list(map(int,input().split()))
res = 0
temp = 0
for i in range(len(nums)):
    temp += nums[i]
    if temp >= k:
        res += 1
        temp = 0
    elif i == len(nums) - 1 and temp > 0:
        res += 1
print(res)