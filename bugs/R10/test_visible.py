import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(initials("Ada Lovelace"), "A.L.")
    def test_double_space(self):
        self.assertEqual(initials("ada  lovelace"), "A.L.")


if __name__ == '__main__':
    unittest.main()
