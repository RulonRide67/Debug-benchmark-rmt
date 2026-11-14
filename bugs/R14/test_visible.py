import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_even(self):
        self.assertEqual(chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
    def test_rest(self):
        self.assertEqual(chunk([1, 2, 3], 2), [[1, 2], [3]])


if __name__ == '__main__':
    unittest.main()
