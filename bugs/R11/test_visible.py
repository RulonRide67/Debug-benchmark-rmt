import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(to_dict(["a=1", "b=2"]), {"a": "1", "b": "2"})
    def test_junk(self):
        self.assertEqual(to_dict(["a=1", "junk"]), {"a": "1"})


if __name__ == '__main__':
    unittest.main()
