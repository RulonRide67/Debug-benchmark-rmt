import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_three(self):
        self.assertEqual(count_down(3), [3, 2, 1])
    def test_zero(self):
        self.assertEqual(count_down(0), [])


if __name__ == '__main__':
    unittest.main()
