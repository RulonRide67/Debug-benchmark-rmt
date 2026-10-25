import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_conflict(self):
        self.assertEqual(merge_dicts({"x": 1}, {"x": 9}), {"x": 9})
    def test_no_mutation(self):
        a = {"x": 1}
        merge_dicts(a, {"y": 2})
        self.assertEqual(a, {"x": 1})


if __name__ == '__main__':
    unittest.main()
