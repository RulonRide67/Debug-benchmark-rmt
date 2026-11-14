import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty_words(self):
        self.assertEqual(total_length(["", "x", ""]), 1)


if __name__ == '__main__':
    unittest.main()
