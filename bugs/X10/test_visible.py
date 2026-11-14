import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_local(self):
        self.assertEqual(safe_redirect("/home"), "/home")
    def test_external(self):
        self.assertEqual(safe_redirect("https://evil.com"), "/")
        self.assertEqual(safe_redirect("//evil.com"), "/")


if __name__ == '__main__':
    unittest.main()
