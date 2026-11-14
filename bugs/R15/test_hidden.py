import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize_tags([]), [])
    def test_float(self):
        self.assertEqual(normalize_tags([3.5]), ["3.5"])


if __name__ == '__main__':
    unittest.main()
