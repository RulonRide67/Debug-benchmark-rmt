import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_edges(self):
        self.assertEqual(clamp(7, 7, 9), 7)
        self.assertEqual(clamp(9, 7, 9), 9)
    def test_float(self):
        self.assertEqual(clamp(8.5, 1, 8), 8)


if __name__ == '__main__':
    unittest.main()
