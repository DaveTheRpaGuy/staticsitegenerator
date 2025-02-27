

def markdown_to_blocks(markdown):
    # Split by double newlines
    blocks = []
    current_block = []
    in_code_block = False
    
    for line in markdown.split("\n"):
        # Check if this line is a code block delimiter
        if line.strip() == "```" or line.strip().startswith("```"):
            in_code_block = not in_code_block
            current_block.append(line)
        # If we're in a code block, add to current block
        elif in_code_block:
            current_block.append(line)
        # If this is an empty line and we're not in a code block, it's a block boundary
        elif line.strip() == "" and not in_code_block and current_block:
            blocks.append("\n".join(current_block))
            current_block = []
        # Otherwise add to current block
        else:
            current_block.append(line)
    
    # Don't forget the last block
    if current_block:
        blocks.append("\n".join(current_block))
    
    return [block.strip() for block in blocks if block.strip()]

