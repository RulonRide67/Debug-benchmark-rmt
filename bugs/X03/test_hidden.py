import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_code_not_executed(self):
        import os
        marker = "pwned_marker.txt"
        if os.path.exists(marker):
            os.remove(marker)
        with self.assertRaises(ValueError):
            parse_number_list("[open('pwned_marker.txt', 'w').close() or 1]")
        self.assertFalse(os.path.exists(marker))
    def test_empty(self):
        self.assertEqual(parse_number_list("[]"), [])
    def test_garbage(self):
        with self.assertRaises(ValueError):
            parse_number_list("[1, 2")


if __name__ == '__main__':
    unittest.main()
