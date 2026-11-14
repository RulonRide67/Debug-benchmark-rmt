import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(second_largest([1, 2, 3]), 2)
    def test_duplicates_visible(self):
        self.assertEqual(second_largest([5, 5, 4]), 4)


if __name__ == '__main__':
    unittest.main()
