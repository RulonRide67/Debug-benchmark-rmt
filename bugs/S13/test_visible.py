import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(describe("Ann", 30), "Ann is 30 years old")
    def test_other(self):
        self.assertEqual(describe("Bo", 7), "Bo is 7 years old")


if __name__ == '__main__':
    unittest.main()
