import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(average([2, 4, 6]), 4)
    def test_tuple(self):
        self.assertEqual(average((1.5,)), 1.5)


if __name__ == '__main__':
    unittest.main()
