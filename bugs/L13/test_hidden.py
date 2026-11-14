import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_strings(self):
        self.assertEqual(unique_in_order(["b", "a", "b"]), ["b", "a"])
    def test_desc(self):
        self.assertEqual(unique_in_order([9, 8, 9, 7]), [9, 8, 7])


if __name__ == '__main__':
    unittest.main()
