from textnode import TextNode, TextType

def main():
    dummy = TextNode("this is some anchor text", TextType.LINK, "http://boot.dev")
    print(dummy)

main()