import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_ten_percent(self):
        self.assertEqual(apply_discount(200, 10), 180.0)


if __name__ == '__main__':
    unittest.main()
