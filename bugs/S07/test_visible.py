import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_values(self):
        self.assertEqual(sign(5), 1)
        self.assertEqual(sign(-2), -1)
        self.assertEqual(sign(0), 0)


if __name__ == '__main__':
    unittest.main()
