import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_a(self):
        self.assertEqual(grade(95), "A")


if __name__ == '__main__':
    unittest.main()
