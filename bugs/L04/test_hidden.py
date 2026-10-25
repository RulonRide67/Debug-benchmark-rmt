import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(apply_discount(50, 0), 50.0)
    def test_full(self):
        self.assertEqual(apply_discount(80, 100), 0.0)
    def test_over(self):
        self.assertEqual(apply_discount(80, 150), 0.0)


if __name__ == '__main__':
    unittest.main()
