import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_c_range(self):
        self.assertEqual(grade(60), "C")
        self.assertEqual(grade(74), "C")
    def test_f(self):
        self.assertEqual(grade(59), "F")


if __name__ == '__main__':
    unittest.main()
