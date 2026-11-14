import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_quotes(self):
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
    def test_empty(self):
        self.assertTrue(is_palindrome(""))
    def test_two(self):
        self.assertFalse(is_palindrome("ab"))


if __name__ == '__main__':
    unittest.main()
