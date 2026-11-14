import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(format_log("bob", "login"), "user=bob action=login")
    def test_newline(self):
        self.assertEqual(format_log("bob\nadmin=1", "login"), "user=bob_admin=1 action=login")


if __name__ == '__main__':
    unittest.main()
