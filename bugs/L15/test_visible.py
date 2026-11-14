import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
    def test_mixed(self):
        self.assertEqual(capitalize_words("hELLO wORLD"), "Hello World")


if __name__ == '__main__':
    unittest.main()
