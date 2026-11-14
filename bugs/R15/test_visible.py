import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(normalize_tags([" Python ", "AI"]), ["python", "ai"])
    def test_number(self):
        self.assertEqual(normalize_tags(["X", 42]), ["x", "42"])


if __name__ == '__main__':
    unittest.main()
