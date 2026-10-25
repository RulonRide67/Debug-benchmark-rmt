import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge_dicts({"x": 1}, {"y": 2}), {"x": 1, "y": 2})


if __name__ == '__main__':
    unittest.main()
