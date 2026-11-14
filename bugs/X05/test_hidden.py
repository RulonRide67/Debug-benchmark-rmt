import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_ip(self):
        self.assertEqual(build_ping_command("8.8.8.8"), ["ping", "-c", "1", "8.8.8.8"])
    def test_more_injection(self):
        for bad in ["a.com && ls", "$(whoami)", "-oProxyCommand=x", "a.com\nls", ""]:
            with self.assertRaises(ValueError):
                build_ping_command(bad)


if __name__ == '__main__':
    unittest.main()
