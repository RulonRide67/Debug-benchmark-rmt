import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_three(self):
        self.assertEqual(initials("Alan Mathison Turing"), "A.M.T.")
    def test_padding(self):
        self.assertEqual(initials(" grace hopper "), "G.H.")
    def test_empty(self):
        self.assertEqual(initials(""), "")


if __name__ == '__main__':
    unittest.main()
