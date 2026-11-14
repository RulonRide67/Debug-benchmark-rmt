import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(shout("hi"), "HI!")
    def test_mixed(self):
        self.assertEqual(shout("Hey you"), "HEY YOU!")


if __name__ == '__main__':
    unittest.main()
