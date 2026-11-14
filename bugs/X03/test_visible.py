import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(parse_number_list("[1, 2.5, 3]"), [1, 2.5, 3])
    def test_string_element(self):
        with self.assertRaises(ValueError):
            parse_number_list("[1, 'a']")
    def test_code_not_executed_visible(self):
        import os
        if os.path.exists("marker_v.txt"):
            os.remove("marker_v.txt")
        with self.assertRaises(ValueError):
            parse_number_list("[open('marker_v.txt', 'w').close() or 1]")
        self.assertFalse(os.path.exists("marker_v.txt"))


if __name__ == '__main__':
    unittest.main()
