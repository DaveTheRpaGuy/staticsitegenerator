import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
            node = ParentNode(
            "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
            self.assertEqual(expected, node.to_html())

    # TODO - Add more unit tests when I feel like it which may be never




