import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_skip(self):
        self.assertEqual(parse_ages("25,30,abc,40"), [25, 30, 40])
    def test_basic(self):
        self.assertEqual(parse_ages("1,2"), [1, 2])


if __name__ == '__main__':
    unittest.main()
