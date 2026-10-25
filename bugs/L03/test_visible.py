import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(second_largest([1, 2, 3]), 2)


if __name__ == '__main__':
    unittest.main()
