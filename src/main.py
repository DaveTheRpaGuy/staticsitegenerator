from textnode import TextNode, TextType

def main():
    print("hello world")
    textnode1 = TextNode("some text", TextType.BOLDTEXT, "https://boot.dev")
    textnode2 = TextNode("dave's text", TextType.ITALICTEXT, "https://davetherpaguy.com")
    
    print(textnode1)
    print(textnode2)

main()