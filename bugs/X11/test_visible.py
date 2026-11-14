import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(repeat_text("ab", 3), "ababab")
    def test_too_long(self):
        with self.assertRaises(ValueError):
            repeat_text("a", 1000000)


if __name__ == '__main__':
    unittest.main()
