import random
class Test:
    def __init__(self):
        self.lists = [1,23,2,4,1,421,412]
    # def __call__(self):
    #     return random.choice(self.lists)
for i in iter(lambda:random.choice(Test().lists),1):
    print(i)
