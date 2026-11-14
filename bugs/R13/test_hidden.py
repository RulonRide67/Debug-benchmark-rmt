import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(cart_total({}, {}), 0)
    def test_only_unknown(self):
        self.assertEqual(cart_total({"x": 3}, {}), 0)


if __name__ == '__main__':
    unittest.main()
