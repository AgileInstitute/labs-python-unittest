import unittest
 
class MyTest(unittest.TestCase):
 
    def test_fun(self):
	self.assertEqual(6, fun(5))

def fun(x):
    return x + 2

if __name__ == '__main__':
    unittest.main()


