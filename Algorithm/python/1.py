#整数反转
def reverse(x: int) -> int:
        a = int(''.join(map(str,list(map(int,str(abs(x))))[::-1])))
        if a<(-2**31) or a>(2**31-1):
            return 0
        return a if x>0 else -a
