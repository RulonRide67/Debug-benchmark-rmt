import unittest
from solution import *


class Visible(unittest.TestCase):
    def setUp(self):
        import sqlite3
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("CREATE TABLE users (id INTEGER, username TEXT)")
        self.conn.executemany("INSERT INTO users VALUES (?, ?)", [(1, "alice"), (2, "o'brien")])
    def test_apostrophe_name(self):
        self.assertEqual(find_user(self.conn, "o'brien"), (2, "o'brien"))


if __name__ == '__main__':
    unittest.main()
