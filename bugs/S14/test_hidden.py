import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(shout(""), "!")


if __name__ == '__main__':
    unittest.main()
