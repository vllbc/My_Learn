# import re

# s = input()
# if re.findall(r"^\d+",s) != []:
#     print("no")
# else:
#     if re.findall(r"[^\w+]",s) != []:
#         print("no")
#     else:
#         print("yes")


m,n = input().split()
nums = []
m,n = int(m),int(n)
for _ in range(m):
    nums.append(list(map(int,input().split())))
res = [[None for _ in range(n)] for _ in range(m)] #新开数组
for i in range(m):
    for j in range(n-2):
        if nums[i][j] == nums[i][j+1] and nums[i][j+1] == nums[i][j+2]:
            res[i][j] = res[i][j+1] = res[i][j+2] = 0
for i in range(n):
    for j in range(m-2):
        if nums[j][i] == nums[j+1][i] and nums[j+1][i] == nums[j+2][i]:
            res[j][i] = res[j+1][i] = res[j+2][i] = 0
for i in range(m):
    for j in range(n):
        if res[i][j] == 0:
            print(0,end=" ")
        else:
            print(nums[i][j],end=' ')
    print("")

