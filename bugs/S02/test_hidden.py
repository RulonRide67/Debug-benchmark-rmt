import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_other(self):
        self.assertEqual(bmi(50, 1.6), 19.5)
    def test_type(self):
        self.assertIsInstance(bmi(80, 2.0), float)


if __name__ == '__main__':
    unittest.main()
