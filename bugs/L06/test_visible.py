import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    def test_others(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(7), "7")


if __name__ == '__main__':
    unittest.main()
