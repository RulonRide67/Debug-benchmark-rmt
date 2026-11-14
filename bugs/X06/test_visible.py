import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_format(self):
        t = generate_token()
        self.assertEqual(len(t), 32)
        int(t, 16)
    def test_not_predictable(self):
        import random
        random.seed(1234)
        a = generate_token()
        random.seed(1234)
        b = generate_token()
        self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
