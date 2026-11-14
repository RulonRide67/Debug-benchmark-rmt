import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_a(self):
        self.assertEqual(grade(95), "A")
    def test_c(self):
        self.assertEqual(grade(70), "C")
        self.assertEqual(grade(60), "C")


if __name__ == '__main__':
    unittest.main()
