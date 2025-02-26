import re

from textnode import TextNode, TextType

def text_to_text_nodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]

    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "*", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
        else:
            split_texts = node.text.split(delimiter)
            if len(split_texts) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for i in range(len(split_texts)):
                if len(split_texts[i]) == 0:
                    continue
                if (i % 2 == 0):
                    new_nodes.append(TextNode(split_texts[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_texts[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
        else:
            regex_results = extract_markdown_images(node.text)
            remaining_text = node.text
            for result in regex_results:
                image_text = f"![{result[0]}]({result[1]})"
                split_texts = remaining_text.split(image_text)
                if len(split_texts[0]) > 0:
                    new_nodes.append(TextNode(split_texts[0], TextType.TEXT))
                new_nodes.append(TextNode(result[0], TextType.IMAGE, result[1]))
                remaining_text = split_texts[1]
            if len(remaining_text) > 0:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
        else:
            regex_results = extract_markdown_links(node.text)
            remaining_text = node.text
            for result in regex_results:
                link_text = f"[{result[0]}]({result[1]})"
                split_texts = remaining_text.split(link_text)
                if len(split_texts[0]) > 0:
                    new_nodes.append(TextNode(split_texts[0], TextType.TEXT))
                new_nodes.append(TextNode(result[0], TextType.LINK, result[1]))
                remaining_text = split_texts[1]
            if len(remaining_text) > 0:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
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