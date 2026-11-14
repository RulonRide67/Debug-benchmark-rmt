import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_hundred(self):
        self.assertEqual(water_state(100), "gas")
    def test_other(self):
        self.assertEqual(water_state(-5), "solid")
        self.assertEqual(water_state(99.9), "liquid")
        self.assertEqual(water_state(150), "gas")


if __name__ == '__main__':
    unittest.main()
