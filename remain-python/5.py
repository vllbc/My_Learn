# name = 'vllbc'
# age = 17
# print(f"{name} {age}")
#斐波那契
def finb(num):
    a=0
    b=1
    
    
    for _ in range(num):
        yield a
        a,b = b,a+b
    
for n in finb(10):
    print(f"{n}\n")

