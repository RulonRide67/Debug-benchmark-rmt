import unittest
from solution import *


class Hidden(unittest.TestCase):
    def setUp(self):
        import sqlite3
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("CREATE TABLE users (id INTEGER, username TEXT)")
        self.conn.executemany("INSERT INTO users VALUES (?, ?)", [(1, "alice"), (2, "bob")])
    def test_normal(self):
        self.assertEqual(find_user(self.conn, "bob"), (2, "bob"))
    def test_injection(self):
        self.assertIsNone(find_user(self.conn, "x' OR '1'='1"))
    def test_missing(self):
        self.assertIsNone(find_user(self.conn, "carol"))


if __name__ == '__main__':
    unittest.main()
