#重点是正则表达式

class Solution:
    def myAtoi(s: str):
        import re
        ss = re.findall("^[\+\-]?\d+",s.strip())
        res = int(*ss)
        if res > (2**31-1):
            res = (2**31-1)
        if res < -2**31:
            res = -2**31
        return res