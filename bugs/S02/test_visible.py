import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(bmi(70, 1.75), 22.9)


if __name__ == '__main__':
    unittest.main()
