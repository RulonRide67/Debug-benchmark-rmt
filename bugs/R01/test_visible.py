import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(average([]))


if __name__ == '__main__':
    unittest.main()
