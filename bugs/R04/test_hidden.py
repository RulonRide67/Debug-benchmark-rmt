import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_two(self):
        out = format_receipt([("a", 1, 0.5), ("b", 3, 2)])
        self.assertEqual(out, "a x1 = 0.50\nb x3 = 6.00\nTOTAL = 6.50")
    def test_empty(self):
        self.assertEqual(format_receipt([]), "TOTAL = 0.00")


if __name__ == '__main__':
    unittest.main()
