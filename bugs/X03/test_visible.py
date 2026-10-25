import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(parse_number_list("[1, 2.5, 3]"), [1, 2.5, 3])
    def test_string_element(self):
        with self.assertRaises(ValueError):
            parse_number_list("[1, 'a']")


if __name__ == '__main__':
    unittest.main()
