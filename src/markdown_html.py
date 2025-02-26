from htmlnode import ParentNode, LeafNode
from block_markdown import markdown_to_blocks
from blocktype import *
from inline_markdown import text_to_text_nodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    nodes = []

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        new_html_node = create_new_html_node(block)
        nodes.append(new_html_node)

    html_node = ParentNode("div", nodes, None)
    return html_node

def create_new_html_node(block):
        block_tag = block_to_tag(block)
        children = text_to_children(block)
        html_node = ParentNode(block_tag, children, None)
        return html_node

def text_to_children(text):
    block_type = block_to_block_type(text)
    text_nodes = text_to_text_nodes(text)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_node = text_node_to_html_node(text_node)
        print("printing leaf_node in text_to_children on next line...")
        print(leaf_node)
        leaf_nodes.append(leaf_node)
    return leaf_nodes