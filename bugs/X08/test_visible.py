import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_expected(self):
        import hashlib
        exp = hashlib.pbkdf2_hmac("sha256", b"secret", b"s1", 100000).hex()
        self.assertEqual(hash_password("secret", "s1"), exp)


if __name__ == '__main__':
    unittest.main()
