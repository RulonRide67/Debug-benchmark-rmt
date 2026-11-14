import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_values(self):
        self.assertTrue(check_api_key("abc", "abc"))
        self.assertFalse(check_api_key("abc", "abd"))
    def test_constant_time(self):
        import inspect
        self.assertIn("compare_digest", inspect.getsource(check_api_key))


if __name__ == '__main__':
    unittest.main()
