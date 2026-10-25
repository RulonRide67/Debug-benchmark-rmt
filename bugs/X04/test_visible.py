import unittest
from solution import *


class Visible(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(render_comment("ann", "nice post"), "<li><b>ann</b>: nice post</li>")
    def test_script_body(self):
        out = render_comment("ann", "<script>alert(1)</script>")
        self.assertNotIn("<script>", out)


if __name__ == '__main__':
    unittest.main()
