#爬楼梯，简单的动态规划

class Solution:
    def PLT(n: str):
        jie = []
        jie.append(1)
        jie.append(2)
        for i in range(2,n):
            jie.append(jie[i-1]+jie[i-2])
        return jie[n-1]
print(Solution.isPalindrome(2))

