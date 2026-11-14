import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_values(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(0), 32)


if __name__ == '__main__':
    unittest.main()
