

def markdown_to_blocks(markdown):
    blocks = []

    blocks = markdown.split("\n\n")

    blocks = [block.strip() for block in blocks]
    
    blocks = list(filter(None, blocks))

    return blocks

