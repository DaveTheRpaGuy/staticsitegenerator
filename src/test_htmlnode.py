import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "Test Heading")
        node2 = HTMLNode("h1", "Test Heading")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("h1", "Test Heading")
        node2 = HTMLNode("h2", "Test Heading")

    def test_props_to_html(self):
        node = HTMLNode("h1", "Test Heading", None, {"href": "https://www.google.com", "target": "_blank"})
        node_html = node.props_to_html()
        self.assertEqual(node_html, " href=\"https://www.google.com\" target=\"_blank\"")

    def test_eq_with_props(self):
        node = HTMLNode("h1", "Test Heading", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h1", "Test Heading", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_neq_with_props(self):
        node = HTMLNode("h1", "Test Heading", None, {"href": "https://www.msn.com", "target": "_blank"})
        node2 = HTMLNode("h1", "Test Heading", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq_with_children(self):
        child_node = HTMLNode("a", "Some Link", None, {"href": "https://www.msn.com", "target": "_blank"})
        child_node2 = HTMLNode("a", "Some Other Link", None, {"href": "https://www.google.com", "target": "_blank"})
        child_nodes = [child_node, child_node2]
        node = HTMLNode("p", None, child_nodes, None)
        node2 = HTMLNode("p", None, child_nodes, None)
        self.assertEqual(node, node2)

    def test_neq_with_children(self):
        child_node = HTMLNode("a", "Some Link", None, {"href": "https://www.msn.com", "target": "_blank"})
        child_node2 = HTMLNode("a", "Some Different Link", None, {"href": "https://www.google.com", "target": "_blank"})
        child_nodes = [child_node, child_node2]
        node = HTMLNode("p", None, child_nodes, None)
        node2 = HTMLNode("h1", None, child_nodes, None)
        self.assertNotEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()