class A:
    def say(self):
        print("I am A")

class B(A):
    def say(self):
    #    super(B, B).say(self)
        super().say()

class C(A):
    def say(self):
        print("I am C")
class D(B, C):
    def say(self):
        super().say() 

D().say()
