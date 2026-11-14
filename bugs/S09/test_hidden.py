import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)


if __name__ == '__main__':
    unittest.main()
