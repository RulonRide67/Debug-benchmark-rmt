import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_city(self):
        self.assertEqual(get_city({"address": {"city": "Astana"}}), "Astana")
    def test_no_address(self):
        self.assertEqual(get_city({"name": "x"}), "unknown")


if __name__ == '__main__':
    unittest.main()
