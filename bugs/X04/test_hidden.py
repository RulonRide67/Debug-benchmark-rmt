import unittest
from solution import *


class Hidden(unittest.TestCase):
    def test_author_escaped(self):
        out = render_comment("<img src=x onerror=alert(1)>", "hi")
        self.assertNotIn("<img", out)
    def test_ampersand_quote(self):
        self.assertEqual(render_comment('a&b', 'say "hi"'),
                         "<li><b>a&amp;b</b>: say &quot;hi&quot;</li>")


if __name__ == '__main__':
    unittest.main()
