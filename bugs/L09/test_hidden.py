import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_zero_negative(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-5))
    def test_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))


if __name__ == '__main__':
    unittest.main()
