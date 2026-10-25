import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_duplicates(self):
        self.assertEqual(second_largest([5, 5, 4]), 4)
    def test_all_same(self):
        self.assertIsNone(second_largest([7, 7]))
    def test_mixed(self):
        self.assertEqual(second_largest([3, 9, 1, 8]), 8)


if __name__ == '__main__':
    unittest.main()
