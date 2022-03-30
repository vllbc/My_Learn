#每次创建count都+1

class Test:
    count = 0
    def __init__(self):
        Test.count += 1

Test()
Test()
print(Test.count)

