import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_list(self):
        self.assertEqual(build_ping_command("example.com"), ["ping", "-c", "1", "example.com"])
    def test_injection(self):
        with self.assertRaises(ValueError):
            build_ping_command("8.8.8.8; rm -rf /")


if __name__ == '__main__':
    unittest.main()
