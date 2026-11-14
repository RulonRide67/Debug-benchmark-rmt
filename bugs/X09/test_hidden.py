import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_lengths(self):
        self.assertFalse(check_api_key("", "x"))
        self.assertTrue(check_api_key("k" * 64, "k" * 64))
    def test_constant_time_used(self):
        import inspect
        self.assertIn("compare_digest", inspect.getsource(check_api_key))


if __name__ == '__main__':
    unittest.main()
