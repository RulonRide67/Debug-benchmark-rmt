import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_2000(self):
        self.assertTrue(is_leap(2000))


if __name__ == '__main__':
    unittest.main()
