import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(water_state(0), "solid")
    def test_mid(self):
        self.assertEqual(water_state(50), "liquid")


if __name__ == '__main__':
    unittest.main()
