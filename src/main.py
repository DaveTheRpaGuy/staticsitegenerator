from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    print("hello world")
    textnode1 = TextNode("some text", TextType.BOLD, "https://boot.dev")
    textnode2 = TextNode("dave's text", TextType.ITALIC, "https://davetherpaguy.com")
    htmlnode1 = HTMLNode("b", "test", None, {"test key": "test value"})
    
    print(textnode1)
    print(textnode2)
    print(htmlnode1)

main()