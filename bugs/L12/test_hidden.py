import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_zero_rate(self):
        self.assertEqual(compound_balance(500, 0, 10), 500.0)
    def test_double(self):
        self.assertEqual(compound_balance(100, 100, 3), 800.0)


if __name__ == '__main__':
    unittest.main()
