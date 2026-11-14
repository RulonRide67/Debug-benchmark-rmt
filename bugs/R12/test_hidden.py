import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(max_score([]))
    def test_negative(self):
        self.assertEqual(max_score([-1, -5]), -1)
    def test_zero(self):
        self.assertEqual(max_score([0, None]), 0)


if __name__ == '__main__':
    unittest.main()
