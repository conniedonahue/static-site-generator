import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_bold_node(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])

    def test_italic_node(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_many_types_one_node(self):
        node = TextNode("This is text with an _italic_ word and a **bold** word and a `code block`", TextType.TEXT)
        italic_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        bold_nodes = split_nodes_delimiter(italic_nodes, "**", TextType.BOLD)
        code_nodes = split_nodes_delimiter(bold_nodes, "`", TextType.CODE)

        self.assertEqual(code_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE)
        ])

    def test_many_types_many_nodes(self):
        node1 = TextNode("This is text with a **bold** word", TextType.TEXT)
        node2 = TextNode("This is text with an _italic_ word", TextType.TEXT)
        node3 = TextNode("This is text with a `code` word", TextType.TEXT)
        bold_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
        print(f"bold nodes: {bold_nodes}")
        italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
        print(f"italic: {italic_nodes}")
        code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
        print(f"code: {code_nodes}")

        self.assertEqual(code_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_missing_matching_delimiter(self):
        node = TextNode('This is an invalid **bold* text', TextType.TEXT)
        with self.assertRaises(ValueError) as cm:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEquals(str(cm.exception), "Invalid Markdown Syntax")

    def test_entire_node_one_style(self):
        node = TextNode("**This entire node is bold**", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_node, [TextNode("This entire node is bold", TextType.BOLD)])

if __name__ == "__main__":
    unittest.main()