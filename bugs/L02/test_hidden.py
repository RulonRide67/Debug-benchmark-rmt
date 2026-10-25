import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_1900(self):
        self.assertFalse(is_leap(1900))
    def test_2024(self):
        self.assertTrue(is_leap(2024))
    def test_2023(self):
        self.assertFalse(is_leap(2023))


if __name__ == '__main__':
    unittest.main()
