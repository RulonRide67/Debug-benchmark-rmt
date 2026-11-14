import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(count_down(-4), [])
    def test_one(self):
        self.assertEqual(count_down(1), [1])


if __name__ == '__main__':
    unittest.main()
