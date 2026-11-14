import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_two_equals(self):
        self.assertEqual(to_dict(["url=x=y"]), {"url": "x=y"})
    def test_empty(self):
        self.assertEqual(to_dict([]), {})


if __name__ == '__main__':
    unittest.main()
