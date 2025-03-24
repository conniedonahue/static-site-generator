import re

def extract_markdown_images(text):
    """
    i: string with MD images
    o: list of tuples (alt, url)

    use regex to find list of 
    """
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    