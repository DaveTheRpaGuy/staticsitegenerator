import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if (is_heading(block)):
        return BlockType.HEADING
    if (is_code(block)):
        return BlockType.CODE
    if (is_quote(block)):
        return BlockType.QUOTE
    if (is_unordered_list(block)):
        return BlockType.UNORDERED_LIST
    if (is_ordered_list(block)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_heading(block):
    regex = r"^#{1,6} .+"
    if re.findall(regex, block):
        return True
    return False

def is_code(block):
    regex = r"^```[\s\S]+```$"
    return re.findall(regex, block)

def is_quote(block):
    for line in block.split("\n"):
        if line.startswith(">") == False:
            return False
    return True

def is_unordered_list(block):
    for line in block.split("\n"):
        if line.startswith("*") == False and line.startswith("-") == False:
            return False
    return True

def is_ordered_list(block):
    previous_number = 0
    regex = r"^(\d+)\. "
    for line in block.split("\n"):
        matches = re.findall(regex, line)
        if (len(matches) == 0):
            return False
        if (int(matches[0]) != previous_number+1):
            return False
        previous_number+=1
    return True

def block_to_tag(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        regex = r"^(#{1,6}) .+"
        matches = re.findall(regex, block)
        return f"h{len(matches[0])}"
    if block_type == BlockType.CODE:
        return "code"
    if block_type == BlockType.QUOTE:
        return "blockquote"
    if block_type == BlockType.UNORDERED_LIST:
        return "ul"
    if block_type == BlockType.ORDERED_LIST:
        return "ol"
    return "p"