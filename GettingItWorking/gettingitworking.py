import unittest
 
class MyTest(unittest.TestCase):
 
    def test_square(self):
	self.assertEqual(4, square(2))
	self.assertEqual(9, square(3))

def square(x):
    return x + x

if __name__ == '__main__':
    unittest.main()


