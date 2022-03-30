class Solution:
    def findContentChildren(g, s) -> int:
        g = sorted(g)
        s = sorted(s)
        n = 0
        for i in range(len(s)):
            if g[n] <= s[i]:
                n += 1
            if n == len(g):
                return n
        return n