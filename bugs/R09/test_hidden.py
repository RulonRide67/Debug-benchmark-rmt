import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(longest_word(["xy", "zw"]), "xy")
    def test_empty_tuple(self):
        self.assertEqual(longest_word(()), "")


if __name__ == '__main__':
    unittest.main()
