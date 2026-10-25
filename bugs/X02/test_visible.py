import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_dotdot(self):
        with self.assertRaises(ValueError):
            safe_path("/srv/files", "../etc/passwd")


if __name__ == '__main__':
    unittest.main()
