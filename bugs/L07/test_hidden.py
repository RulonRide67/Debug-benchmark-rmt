import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_symmetric(self):
        self.assertEqual(sum_range(-2, 2), 0)
    def test_other(self):
        self.assertEqual(sum_range(5, 7), 18)


if __name__ == '__main__':
    unittest.main()
