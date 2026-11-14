import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_userinfo(self):
        self.assertFalse(is_allowed_url("https://api.example.com@evil.net/"))
    def test_case_and_port(self):
        self.assertTrue(is_allowed_url("https://API.example.com/v1"))
        self.assertTrue(is_allowed_url("https://api.example.com:443/v1"))


if __name__ == '__main__':
    unittest.main()
