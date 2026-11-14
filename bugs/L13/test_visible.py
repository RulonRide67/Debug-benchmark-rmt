import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_order(self):
        self.assertEqual(unique_in_order([3, 1, 3, 2, 1]), [3, 1, 2])
    def test_empty(self):
        self.assertEqual(unique_in_order([]), [])


if __name__ == '__main__':
    unittest.main()
