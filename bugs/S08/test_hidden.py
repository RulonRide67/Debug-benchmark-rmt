import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_new_object(self):
        a = default_config()
        a["port"] = 1
        self.assertEqual(default_config()["port"], 8080)


if __name__ == '__main__':
    unittest.main()
