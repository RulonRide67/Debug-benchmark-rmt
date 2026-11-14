import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_empty_address(self):
        self.assertEqual(get_city({"address": {}}), "unknown")
    def test_none_address(self):
        self.assertEqual(get_city({"address": None}), "unknown")


if __name__ == '__main__':
    unittest.main()
