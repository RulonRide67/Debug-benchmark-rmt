import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_single(self):
        self.assertEqual(reverse_words("one"), "one")
    def test_empty(self):
        self.assertEqual(reverse_words(""), "")
    def test_four(self):
        self.assertEqual(reverse_words("w x y z"), "z y x w")


if __name__ == '__main__':
    unittest.main()
