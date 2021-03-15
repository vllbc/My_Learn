class Test:
    @classmethod
    def wrapper1(cls):
        print("ok")

    class wrapper2:
        def __init__(self):
            print("ok")

Test.wrapper1()
Test.wrapper2()