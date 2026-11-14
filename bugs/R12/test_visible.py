import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_with_none(self):
        self.assertEqual(max_score([3, None, 7]), 7)
    def test_all_none(self):
        self.assertIsNone(max_score([None, None]))


if __name__ == '__main__':
    unittest.main()
