import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(remove_empty({"a": "", "b": "x"}), {"b": "x"})


if __name__ == '__main__':
    unittest.main()
