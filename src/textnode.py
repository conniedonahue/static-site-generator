from enum import Enum
from htmlnode import HTMLNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
         return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
        match(text_node.text_type):
            case TextType.TEXT:
                tag = None
            case TextType.BOLD:
                tag = 'b'
            case TextType.ITALIC:
                tag = 'i'
            case TextType.CODE:
                tag = 'code'
            case TextType.LINK:
                tag = "a"
            case TextType.IMAGE:
                if not text_node.url:
                    raise ValueError('Missing required "src" property in TextType.IMAGE props')
                if not text_node.text:
                    raise ValueError('Missing required "alt" property in TextType.IMAGE props')
                return HTMLNode("img", None, None, {'src': text_node.url, 'alt': text_node.text})
            case _:
                raise ValueError(f"Invalid TextType: {text_node.text_type}")

        return HTMLNode(tag, text_node.text, None, None)