import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_one_year(self):
        self.assertEqual(compound_balance(1000, 10, 1), 1100.0)
    def test_two_years(self):
        self.assertEqual(compound_balance(1000, 5, 2), 1102.5)


if __name__ == '__main__':
    unittest.main()
