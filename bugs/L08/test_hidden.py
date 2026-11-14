import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_single(self):
        self.assertEqual(median([5]), 5)
    def test_two(self):
        self.assertEqual(median([1, 2]), 1.5)
    def test_six(self):
        self.assertEqual(median([7, 1, 5, 3, 9, 11]), 6.0)


if __name__ == '__main__':
    unittest.main()
