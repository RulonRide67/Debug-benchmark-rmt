import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_case(self):
        self.assertEqual(word_counts("Hi hi HI"), {"hi": 3})
    def test_empty(self):
        self.assertEqual(word_counts(""), {})


if __name__ == '__main__':
    unittest.main()
