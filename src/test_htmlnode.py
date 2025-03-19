import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode('a', "inner text", [], "www.google.com")
        node2 = HTMLNode('a', "inner text", [], "www.google.com")
        self.assertEqual(node1, node2)
    
    def test_eq_false1(self):
        node1 = HTMLNode('b', "inner text", [], "www.google.com")
        node2 = HTMLNode('a', "inner text", [], "www.google.com")
        self.assertNotEqual(node1, node2)

    def test_eq_false2(self):
        node1 = HTMLNode('a', "inner text", [], "www.google.com")
        node2 = HTMLNode('a', "other inner text", [], "www.google.com")
        self.assertNotEqual(node1, node2)

    def test_eq_false3(self):
        node1 = HTMLNode('a', "inner text", ["child"], {"href": "www.google.com"})
        node2 = HTMLNode('a', "inner text", [], {"href": "www.google.com"})
        self.assertNotEqual(node1, node2)

    def test_eq_false4(self):
        node1 = HTMLNode('a', "inner text", [], {"href": "www.google.com"})
        node2 = HTMLNode('a', "inner text", [], {"href": "www.bing.com"})
        self.assertNotEqual(node1, node2)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

class TestPropsToHTML(unittest.TestCase):
    def test_correct(self):
        node1 = HTMLNode('a', "inner text", [], {"href": "www.google.com", "target": "_blank"})
        res = node1.props_to_html()

        self.assertEqual(res, ' href="www.google.com" target="_blank"')
    
    def test_empty(self):
        node1 = HTMLNode('a', "inner text", [], {})
        res = node1.props_to_html()

        self.assertEqual(res, '')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_granchilden_and_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"id": "bold-text"})
        child_node = ParentNode("span", [grandchild_node], {'className':"p-4"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span className="p-4"><b id="bold-text">grandchild</b></span></div>',
        )

    def test_to_html_ValueError_no_children(self):
        parent_node = ParentNode(None, None, None)
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(str(cm.exception), "Missing tag")

if __name__ == "__main__":
    unittest.main()
