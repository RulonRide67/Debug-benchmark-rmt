import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_name(self):
        self.assertEqual(update_profile({"name": "a", "is_admin": False}, {"name": "b"}),
                         {"name": "b", "is_admin": False})
    def test_admin_ignored(self):
        p = update_profile({"name": "a", "is_admin": False}, {"is_admin": True})
        self.assertFalse(p["is_admin"])


if __name__ == '__main__':
    unittest.main()
