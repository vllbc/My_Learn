#1
class Solution:
    def removeDuplicateLetters(s: str):
        res = ""
        while s: #用递归也可以
            loc = min(map(s.rindex,s)) #s.rindex是返回列表各值最后出现的索引 求这个最小的索引
            a = min(s[:loc+1]) #求字典序最小的
            res += a
            s = s[s.index(a):].replace(a,"") #把已经加入的和与其重复的都去掉了
        return res



#2
#遍历字符串，压入栈，如果遇到比栈顶小的元素且当前字符后面还有与栈顶相同的元素时，移除栈顶元素
class Solution:
    def removeDuplicateLetters(s: str) -> str:
        stack = []
        for i, t in enumerate(s):
            if t in stack:
                continue
            while stack !=[] and t < stack[-1] and s[i:].find(stack[-1]) != -1:
                stack.pop()
            stack.append(t)
        return "".join(stack)