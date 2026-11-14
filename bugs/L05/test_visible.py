import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_case(self):
        self.assertTrue(is_palindrome("Racecar"))
    def test_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
    def test_false(self):
        self.assertFalse(is_palindrome("hello"))


if __name__ == '__main__':
    unittest.main()
