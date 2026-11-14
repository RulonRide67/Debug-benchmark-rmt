import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_three(self):
        self.assertEqual(first_n_squares(3), [0, 1, 4])
    def test_zero(self):
        self.assertEqual(first_n_squares(0), [])


if __name__ == '__main__':
    unittest.main()
