import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(longest_word(["a", "abc", "ab"]), "abc")
    def test_empty(self):
        self.assertEqual(longest_word([]), "")


if __name__ == '__main__':
    unittest.main()
