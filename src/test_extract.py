import unittest
from extract import extract_markdown_images, extract_markdown_links

class TestExtractFunctions(unittest.TestCase):

    def test_extract_markdown_images_one(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_many(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://imgur.com/gallery/car-is-charging-k7WxskQ#/t/aww)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://imgur.com/gallery/car-is-charging-k7WxskQ#/t/aww")], matches)

    def test_extract_markdown_images_with_link(self):
        matches = extract_markdown_images(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_one(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_markdown_links_many(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com) and [link2](www.yahoo.com)"
        )
        self.assertListEqual([("link", "https://www.google.com"),("link2", "www.yahoo.com")], matches)

    def test_extract_markdown_links_with_link_and_image(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_markdown_links_with_image(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)