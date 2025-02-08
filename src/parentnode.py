from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is required")
        if not self.children:
            raise ValueError("children is required")
        output = f"<{self.tag}>"
        for child in self.children:
            output+=child.to_html()
        output += f"</{self.tag}>"
        return output
