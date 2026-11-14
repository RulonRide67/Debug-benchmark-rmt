import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(cart_total({"apple": 2}, {"apple": 1.5}), 3.0)
    def test_unknown(self):
        self.assertEqual(cart_total({"apple": 2, "kiwi": 1}, {"apple": 1.5}), 3.0)


if __name__ == '__main__':
    unittest.main()
