class Solution:
    def countAndSay(self,n: int):
        if n == 1:
           return '1'
        s = self.countAndSay(n - 1)
        n,res = 0,''
        for ii,ss in enumerate(s):
            if ss != s[n]:
                res += str(ii-n) + s[n]
                n = ii
        res += str(len(s) - n) + s[-1]
        return res
print(Solution().countAndSay(3))