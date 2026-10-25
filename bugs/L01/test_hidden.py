import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_last(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 7), 3)
    def test_absent(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 4), -1)
    def test_empty(self):
        self.assertEqual(binary_search([], 1), -1)


if __name__ == '__main__':
    unittest.main()
