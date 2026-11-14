import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(pair_averages([(1, 3), (2, 2)]), [2.0, 2.0])


if __name__ == '__main__':
    unittest.main()
