import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parse_ages(""), [])
    def test_float(self):
        self.assertEqual(parse_ages("3.5,4"), [4])
    def test_spaces(self):
        self.assertEqual(parse_ages(" 7 , 8 "), [7, 8])


if __name__ == '__main__':
    unittest.main()
