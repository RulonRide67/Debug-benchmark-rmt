import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_single(self):
        self.assertEqual(differences([7]), [])
    def test_empty(self):
        self.assertEqual(differences([]), [])
    def test_negative(self):
        self.assertEqual(differences([5, 2]), [-3])


if __name__ == '__main__':
    unittest.main()
