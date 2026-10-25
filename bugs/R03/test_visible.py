import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(differences([1, 4, 9]), [3, 5])


if __name__ == '__main__':
    unittest.main()
