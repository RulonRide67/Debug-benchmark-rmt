import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_token_removed(self):
        import json
        out = json.loads(user_to_json({"name": "a", "token": "t", "age": 3}))
        self.assertEqual(out, {"name": "a", "age": 3})
    def test_not_modified(self):
        u = {"name": "a", "password": "p"}
        user_to_json(u)
        self.assertEqual(u, {"name": "a", "password": "p"})


if __name__ == '__main__':
    unittest.main()
