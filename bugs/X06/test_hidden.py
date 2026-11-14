import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_not_predictable_other_seed(self):
        import random
        random.seed(0)
        a = generate_token()
        random.seed(0)
        self.assertNotEqual(a, generate_token())
    def test_unique(self):
        self.assertEqual(len({generate_token() for _ in range(50)}), 50)


if __name__ == '__main__':
    unittest.main()
