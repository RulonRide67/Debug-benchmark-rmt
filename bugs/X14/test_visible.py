import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_ok(self):
        self.assertTrue(is_allowed_url("https://api.example.com/v1/items"))
    def test_bad(self):
        self.assertFalse(is_allowed_url("http://api.example.com/v1"))
        self.assertFalse(is_allowed_url("https://api.example.com.evil.net/v1"))


if __name__ == '__main__':
    unittest.main()
