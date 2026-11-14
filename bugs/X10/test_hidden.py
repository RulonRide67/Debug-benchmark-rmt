import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_backslash(self):
        self.assertEqual(safe_redirect("/\\evil.com"), "/")
    def test_query(self):
        self.assertEqual(safe_redirect("/a/b?x=1"), "/a/b?x=1")
    def test_empty(self):
        self.assertEqual(safe_redirect(""), "/")


if __name__ == '__main__':
    unittest.main()
