import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_cr(self):
        self.assertEqual(format_log("a\rb", "x"), "user=a_b action=x")
    def test_action(self):
        self.assertEqual(format_log("a", "x\ny\r\nz"), "user=a action=x_y__z")


if __name__ == '__main__':
    unittest.main()
