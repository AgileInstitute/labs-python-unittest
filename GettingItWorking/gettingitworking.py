import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        self.my_maths = MyMaths()
 
    def test_squares_two(self):
        self.assertEqual(4, self.my_maths.square(2))

    def test_squares_three(self):
        self.assertEqual(9, self.my_maths.square(3))

class MyMaths:
    def square(self, x):
        return x + x



if __name__ == '__main__':
    unittest.main()


