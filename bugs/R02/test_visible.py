import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(word_counts("a b a"), {"a": 2, "b": 1})


if __name__ == '__main__':
    unittest.main()
