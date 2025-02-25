import re

from textnode import TextNode, TextType
        
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.IMAGE.value:
            new_nodes.append(node)
        else:
            split_texts = node.text.split(delimiter)
            if len(split_texts) == 3:
                new_nodes.append(TextNode(split_texts[0], TextType.TEXT))
                new_nodes.append(TextNode(split_texts[1], TextType.IMAGE))
                new_nodes.append(TextNode(split_texts[2], TextType.TEXT))
            elif len(split_texts) == 2:
                raise Exception("invalid markdown syntax")
            else:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.LINK.value:
            new_nodes.append(node)
        else:
            something = ""
    return new_nodes

def extract_markdown_images(text):
    regex = r"!\[([\w\s]+?)\]\((\w+:\/\/.*?)\)"
    matches = re.findall(regex, text)
    #print("print image matches...")
    #print(matches)
    return matches

def extract_markdown_links(text):
    regex = r"[^!]\[([\w\s]+?)\]\((\w+:\/\/.*?)\)"
    #print("print link matches...")
    matches = re.findall(regex, text)
    return matches