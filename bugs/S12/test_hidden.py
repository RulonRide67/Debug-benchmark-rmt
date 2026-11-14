import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(pair_averages([]), [])
    def test_float(self):
        self.assertEqual(pair_averages([(0, 1)]), [0.5])


if __name__ == '__main__':
    unittest.main()
