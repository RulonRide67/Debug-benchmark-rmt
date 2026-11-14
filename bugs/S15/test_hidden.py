import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_middle(self):
        self.assertEqual(max_of_three(1, 8, 3), 8)
    def test_equal(self):
        self.assertEqual(max_of_three(-1, -1, -1), -1)


if __name__ == '__main__':
    unittest.main()
