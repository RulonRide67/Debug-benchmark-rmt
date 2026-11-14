import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_words("a b c"), "c b a")
    def test_spaces(self):
        self.assertEqual(reverse_words("  hello   world "), "world hello")


if __name__ == '__main__':
    unittest.main()
