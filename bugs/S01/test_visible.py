import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_vowels("hello"), 2)


if __name__ == '__main__':
    unittest.main()
