import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sum_range(1, 3), 6)
    def test_single(self):
        self.assertEqual(sum_range(2, 2), 2)


if __name__ == '__main__':
    unittest.main()
