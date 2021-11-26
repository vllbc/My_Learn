def say_hello(name=None):
    if name:
        return f"hello {name}"
    return "hello world"


import unittest
from typing import List


class sayhellotest(unittest.TestCase):
    def setUp(self,nums:List[int] = 0):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_sayhello(self):
        rv = say_hello()
        self.assertEqual(rv,"hello world")
    
    def test_to_name(self):
        rv = say_hello("wlb")
        self.assertEqual(rv,"hello wlb")
    

if __name__ == '__main__':
    unittest.main()