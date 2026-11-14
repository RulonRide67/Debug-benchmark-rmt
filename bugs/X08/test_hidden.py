import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(hash_password("a", "b")), 64)
    def test_salt_matters(self):
        self.assertNotEqual(hash_password("pw", "x"), hash_password("pw", "y"))
    def test_unicode(self):
        import hashlib
        exp = hashlib.pbkdf2_hmac("sha256", "caf\u00e9".encode(), b"z", 100000).hex()
        self.assertEqual(hash_password("caf\u00e9", "z"), exp)


if __name__ == '__main__':
    unittest.main()
