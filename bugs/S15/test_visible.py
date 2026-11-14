import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_last(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
    def test_first(self):
        self.assertEqual(max_of_three(9, 2, 3), 9)


if __name__ == '__main__':
    unittest.main()
