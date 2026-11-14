import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_mixed(self):
        p = update_profile({"name": "a", "role": "user"}, {"bio": "hi", "role": "admin", "id": 1})
        self.assertEqual(p, {"name": "a", "role": "user", "bio": "hi"})
    def test_empty(self):
        self.assertEqual(update_profile({"x": 1}, {}), {"x": 1})


if __name__ == '__main__':
    unittest.main()
