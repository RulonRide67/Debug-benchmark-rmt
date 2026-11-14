import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_inside(self):
        self.assertEqual(clamp(5, 0, 10), 5)
    def test_outside(self):
        self.assertEqual(clamp(-3, 0, 10), 0)
        self.assertEqual(clamp(15, 0, 10), 10)


if __name__ == '__main__':
    unittest.main()
