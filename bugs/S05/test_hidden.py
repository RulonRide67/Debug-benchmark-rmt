import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_five(self):
        self.assertEqual(first_n_squares(5), [0, 1, 4, 9, 16])


if __name__ == '__main__':
    unittest.main()
