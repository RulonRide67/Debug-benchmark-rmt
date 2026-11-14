import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(greet("Ann"), "Hello, Ann!")
    def test_other(self):
        self.assertEqual(greet("Bob"), "Hello, Bob!")


if __name__ == '__main__':
    unittest.main()
