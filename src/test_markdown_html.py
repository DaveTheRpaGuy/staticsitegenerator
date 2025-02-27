import unittest

from markdown_html import *

class TestMarkdownHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )
    
    def test_markdown_to_html_node_given_by_lesson(self):
        markdown = """
## This is a heading 2

This is a **paragraph**

"""

        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        expected = "<div><h2>This is a heading 2</h2><p>This is a <b>paragraph</b></p></div>"
        self.assertEqual(expected, actual)
    