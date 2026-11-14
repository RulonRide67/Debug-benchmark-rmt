import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_pickle_payload(self):
        import os, pickle
        class Payload:
            def __reduce__(self):
                return (open, ("pwned_pickle.txt", "w"))
        data = pickle.dumps(Payload())
        if os.path.exists("pwned_pickle.txt"):
            os.remove("pwned_pickle.txt")
        with self.assertRaises(ValueError):
            load_settings(data)
        self.assertFalse(os.path.exists("pwned_pickle.txt"))
    def test_garbage(self):
        with self.assertRaises(ValueError):
            load_settings(b'{not json')


if __name__ == '__main__':
    unittest.main()
