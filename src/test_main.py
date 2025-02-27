import unittest

from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = """
Some words

Some more words
# The Heading
And more stuff

and more
"""

        expected = "The Heading"
        actual = extract_title(markdown)
        self.assertEqual(expected, actual)