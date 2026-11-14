import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_30(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
    def test_more(self):
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(10), "Buzz")


if __name__ == '__main__':
    unittest.main()
