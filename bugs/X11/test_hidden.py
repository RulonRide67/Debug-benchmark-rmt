import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_negative(self):
        with self.assertRaises(ValueError):
            repeat_text("x", -1)
    def test_limit(self):
        self.assertEqual(len(repeat_text("abc", 3333)), 9999)
        with self.assertRaises(ValueError):
            repeat_text("abc", 3334)
    def test_empty_text(self):
        self.assertEqual(repeat_text("", 10**9), "")


if __name__ == '__main__':
    unittest.main()
