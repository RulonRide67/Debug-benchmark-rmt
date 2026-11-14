import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_five(self):
        self.assertEqual(factorial(5), 120)
    def test_zero(self):
        self.assertEqual(factorial(0), 1)


if __name__ == '__main__':
    unittest.main()
