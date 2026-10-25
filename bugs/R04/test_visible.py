import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_one(self):
        self.assertEqual(format_receipt([("tea", 2, 1.5)]), "tea x2 = 3.00\nTOTAL = 3.00")


if __name__ == '__main__':
    unittest.main()
