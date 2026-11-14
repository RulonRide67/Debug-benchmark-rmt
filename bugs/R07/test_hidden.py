import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_one(self):
        self.assertEqual(factorial(1), 1)
    def test_ten(self):
        self.assertEqual(factorial(10), 3628800)
    def test_zero_again(self):
        self.assertEqual(factorial(0) * 2, 2)


if __name__ == '__main__':
    unittest.main()
