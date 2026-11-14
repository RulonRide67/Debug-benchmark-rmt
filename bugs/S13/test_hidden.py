import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(describe("Cy", 0), "Cy is 0 years old")


if __name__ == '__main__':
    unittest.main()
