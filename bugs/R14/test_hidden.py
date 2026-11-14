import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(chunk([], 3), [])
    def test_large(self):
        self.assertEqual(chunk([1], 5), [[1]])


if __name__ == '__main__':
    unittest.main()
