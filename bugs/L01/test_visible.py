import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_single(self):
        self.assertEqual(binary_search([5], 5), 0)


if __name__ == '__main__':
    unittest.main()
