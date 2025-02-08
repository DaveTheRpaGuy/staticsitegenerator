from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid text node")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
        else:
            split_texts = node.text.split(delimiter)
            if len(split_texts) == 3:
                new_nodes.append(TextNode(split_texts[0], TextType.TEXT))
                new_nodes.append(TextNode(split_texts[1], text_type))
                new_nodes.append(TextNode(split_texts[2], TextType.TEXT))
            elif len(split_texts) == 2:
                raise Exception("invalid markdown syntax")
            else:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes