import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_password_removed(self):
        import json
        out = json.loads(user_to_json({"name": "a", "password": "p"}))
        self.assertEqual(out, {"name": "a"})


if __name__ == '__main__':
    unittest.main()
