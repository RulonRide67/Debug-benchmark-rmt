import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_json(self):
        self.assertEqual(load_settings(b'{"theme": "dark", "size": 12}'), {"theme": "dark", "size": 12})
    def test_not_object(self):
        with self.assertRaises(ValueError):
            load_settings(b'[1, 2]')


if __name__ == '__main__':
    unittest.main()
