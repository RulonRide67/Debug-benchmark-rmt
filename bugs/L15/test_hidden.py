import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(capitalize_words("PYTHON is FUN"), "Python Is Fun")
    def test_single(self):
        self.assertEqual(capitalize_words("a"), "A")


if __name__ == '__main__':
    unittest.main()
