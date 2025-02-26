import unittest

from block_markdown import *

class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_blocks_basic(self):
        markdown = "# This is a heading"\
            "\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it."\
            "\n\n* This is the first list item in a list block"\
            "\n* This is a list item"\
            "\n* This is another list item"
        
        actual = markdown_to_blocks(markdown)

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block"\
            "\n* This is a list item"\
            "\n* This is another list item"
        ]
        
        self.assertListEqual(expected, actual)

    def test_markdown_to_blocks_leading_trailing_whitespace(self):
        markdown = "       # This is a heading"\
            "\n\n  This is a paragraph of text. It has some **bold** and *italic* words inside of it.  "\
            "\n\n* This is the first list item in a list block"\
            "\n* This is a list item"\
            "\n* This is another list item  "
        
        actual = markdown_to_blocks(markdown)

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block"\
            "\n* This is a list item"\
            "\n* This is another list item"
        ]
        
        self.assertListEqual(expected, actual)

    def test_markdown_to_blocks_empty_blocks(self):
        markdown = "       # This is a heading"\
            "\n\n  This is a paragraph of text. It has some **bold** and *italic* words inside of it.  "\
            "\n\n"\
            "\n\n* This is the first list item in a list block"\
            "\n* This is a list item"\
            "\n* This is another list item  "
        
        actual = markdown_to_blocks(markdown)

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block"\
            "\n* This is a list item"\
            "\n* This is another list item"
        ]
        
        self.assertListEqual(expected, actual)


        def test_markdown_to_blocks(self):
            md = """
                This is **bolded** paragraph

                This is another paragraph with *italic* text and `code` here
                This is the same paragraph on a new line

                * This is a list
                * with items
                """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                    "* This is a list\n* with items",
                ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )