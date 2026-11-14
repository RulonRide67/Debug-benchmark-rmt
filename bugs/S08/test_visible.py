import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_config(self):
        self.assertEqual(default_config(), {"host": "localhost", "port": 8080, "debug": False})


if __name__ == '__main__':
    unittest.main()
