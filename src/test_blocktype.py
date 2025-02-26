import unittest

from blocktype import *


class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_basic_paragraph(self):
        expected = BlockType.PARAGRAPH
        block_text = "blah blah blah this is a paragraph"\
            "\nsome other stuff blah blah"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)
    
    def test_block_to_block_type_heading_one(self):
        expected = BlockType.HEADING
        block_text = "# BlahBlah"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)
    
    def test_block_to_block_type_not_heading_because_no_space(self):
        expected = BlockType.PARAGRAPH
        block_text = "#BlahBlah"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_heading_six(self):
        expected = BlockType.HEADING
        block_text = "###### BlahBlah"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_heading_seven_is_paragraph(self):
        expected = BlockType.PARAGRAPH
        block_text = "####### BlahBlah"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_quote(self):
        expected = BlockType.QUOTE
        block_text = "> BlahBlah\n> Another line"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_quote_is_paragraph(self):
        expected = BlockType.PARAGRAPH
        block_text = "> BlahBlah\n> Another line\nThis line makes it not a quote"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_unordered_list_asterisk(self):
        expected = BlockType.UNORDERED_LIST
        block_text = "* BlahBlah\n* Another line"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_unordered_list_hyphen(self):
        expected = BlockType.UNORDERED_LIST
        block_text = "- BlahBlah\n- Another line"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_not_unordered_list(self):
        expected = BlockType.PARAGRAPH
        block_text = "- BlahBlah\n+ This makes it not unordered list\n- Another line"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_ordered_list(self):
        expected = BlockType.ORDERED_LIST
        block_text = "1. BlahBlah\n2. Another line\n3. Third line"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_not_ordered_list(self):
        expected = BlockType.PARAGRAPH
        block_text = "1. BlahBlah\n4. This makes it not ordered list\n3. Third line"
        actual = block_to_block_type(block_text)
        self.assertEqual(expected, actual)