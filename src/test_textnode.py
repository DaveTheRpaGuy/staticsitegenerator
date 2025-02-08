import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("Some text", TextType.BOLD)
        node2 = TextNode("Some text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Some text", TextType.CODE, "https://davetherpaguy.com")
        node2 = TextNode("Some text", TextType.CODE, "https://davetherpaguy.com")
        self.assertEqual(node, node2)

    def test_neq_with_url(self):
        node = TextNode("Some text", TextType.CODE, "https://davetherpaguy.com")
        node2 = TextNode("Some text", TextType.CODE, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_neq_no_and_url(self):
        node = TextNode("Some text", TextType.NORMAL, "https://davetherpaguy.com")
        node2 = TextNode("Some text", TextType.NORMAL)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()