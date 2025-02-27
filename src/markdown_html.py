from htmlnode import ParentNode, LeafNode
from block_markdown import markdown_to_blocks
from blocktype import *
from inline_markdown import text_to_text_nodes
from textnode import *

def markdown_to_html_node(markdown):
    nodes = []

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        new_html_node = create_new_html_node(block)
        nodes.append(new_html_node)

    html_node = ParentNode("div", nodes, None)
    return html_node

def create_new_html_node(block):
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            block_tag = block_to_tag(block)
            cleaned_block = re.sub(r'^#{1,6} ', '', block)
            item_children = text_to_children(cleaned_block)
            parent_heading_node = ParentNode(block_tag, item_children, None)
            return parent_heading_node
        
        if block_type == BlockType.CODE:
            code_content = extract_code_content(block)
            code_text_node = TextNode(code_content, TextType.TEXT)
            code_leaf_node = text_node_to_html_node(code_text_node)
            parent_pre_node = ParentNode("pre", [code_leaf_node], None)
            return parent_pre_node
        
        if block_type == BlockType.QUOTE:
            block_tag = block_to_tag(block)
            cleaned_block = re.sub(r'^> ', '', block, re.M)
            item_children = text_to_children(cleaned_block)
            parent_quote_node = ParentNode(block_tag, item_children, None)
            return parent_quote_node

        if block_type in [BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST]:
            block_tag = block_to_tag(block)
            items = extract_list_items(block)
            item_nodes = []
            for item in items:
                item_children = text_to_children(item)
                item_parent_node = ParentNode("li", item_children, None)
                item_nodes.append(item_parent_node)
            parent_list_node = ParentNode(block_tag, item_nodes, None)
            return parent_list_node
        
        if block_type == BlockType.PARAGRAPH:
            block_tag = block_to_tag(block)
            cleaned_block = re.sub(r'\n', ' ', block)
            item_children = text_to_children(cleaned_block)
            parent_paragraph_node = ParentNode(block_tag, item_children, None)
            return parent_paragraph_node

def extract_code_content(block):
    regex = r"^```([\s\S]*)```$"
    matches = re.findall(regex, block)
    return matches[0]

def extract_list_items(block):
    items = []
    for item in block.split("\n"):
        cleaned_item = re.sub(r'^\d+\. |^\*|^\-', '', item)
        items.append(cleaned_item) 
    return items

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_node = text_node_to_html_node(text_node)
        leaf_nodes.append(leaf_node)
    return leaf_nodes