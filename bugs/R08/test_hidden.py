import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_all_empty(self):
        self.assertEqual(remove_empty({"a": "", "b": ""}), {})
    def test_none_empty(self):
        self.assertEqual(remove_empty({"a": "1"}), {"a": "1"})
    def test_in_place(self):
        d = {"a": "", "b": "y"}
        remove_empty(d)
        self.assertEqual(d, {"b": "y"})


if __name__ == '__main__':
    unittest.main()
