import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_case(self):
        self.assertEqual(count_vowels("AEIOU xyz"), 5)
    def test_empty(self):
        self.assertEqual(count_vowels(""), 0)


if __name__ == '__main__':
    unittest.main()
