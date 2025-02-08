import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("h1", "Test Heading")
        node2 = LeafNode("h1", "Test Heading")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = LeafNode("h1", "Test Heading")
        node2 = LeafNode("h2", "Test Heading")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = LeafNode("h1", "Test Heading", {"href": "https://www.google.com", "target": "_blank"})
        node_html = node.props_to_html()
        self.assertEqual(node_html, " href=\"https://www.google.com\" target=\"_blank\"")

    def test_eq_with_props(self):
        node = LeafNode("h1", "Test Heading", {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode("h1", "Test Heading", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_neq_with_props(self):
        node = LeafNode("h1", "Test Heading", {"href": "https://www.msn.com", "target": "_blank"})
        node2 = LeafNode("h1", "Test Heading", {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()