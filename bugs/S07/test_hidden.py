import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_float(self):
        self.assertEqual(sign(-0.5), -1)
        self.assertEqual(sign(1e-9), 1)


if __name__ == '__main__':
    unittest.main()
