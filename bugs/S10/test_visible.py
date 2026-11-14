import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(total_length(["ab", "cde"]), 5)
    def test_empty(self):
        self.assertEqual(total_length([]), 0)


if __name__ == '__main__':
    unittest.main()
