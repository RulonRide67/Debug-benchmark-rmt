import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_one(self):
        self.assertFalse(is_prime(1))
    def test_basic(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(9))


if __name__ == '__main__':
    unittest.main()
