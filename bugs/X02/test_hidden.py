import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_absolute(self):
        with self.assertRaises(ValueError):
            safe_path("/srv/files", "/etc/passwd")
    def test_normal(self):
        import os
        self.assertEqual(safe_path("/srv/files", "a/b.txt"),
                         os.path.realpath("/srv/files/a/b.txt"))
    def test_inner_dotdot_ok(self):
        import os
        self.assertEqual(safe_path("/srv/files", "a/../c.txt"),
                         os.path.realpath("/srv/files/c.txt"))
    def test_prefix_trick(self):
        with self.assertRaises(ValueError):
            safe_path("/srv/files", "../files_secret/x")


if __name__ == '__main__':
    unittest.main()
