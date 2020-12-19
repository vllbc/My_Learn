#回文字符串，正则表达式去掉特殊符号
class Solution:
    def isPalindrome(s: str):
        if s.strip() == '':
            return True
        import re
        strs = re.sub(r"[^a-zA-Z0-9]","",s).lower()
        return strs[::-1] == strs
print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
