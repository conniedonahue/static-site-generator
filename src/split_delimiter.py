from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    define output list
    iterate through old_nodes list
    check to see if type = text
      if not, push to list
      if so:
        iterate through chars in str until you find delimiter
        previous bit become a textnode type text
        keep iterating until you find the matching delimiter
          if you don't find one, raise exception

    """
    output = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
        l, r = 0, 0
        open_delimiter = False
        while r < len(node.text):
            if node.text[r] != delimiter:
                r += 1
            elif node.text[r] == delimiter and open_delimiter == False:
                open_delimiter = True
                output.append(TextNode(node.text[l:r], TextType.TEXT))
                l = r + 1
                r += 1
            elif node.text[r] == delimiter and open_delimiter == True:
                open_delimiter = False
                output.append(TextNode(node.text[l:r], text_type))
                l = r + 1
                r += 1
        if open_delimiter == True:
            raise ValueError("Invalid Markdown Syntax")
        elif open_delimiter == False and l < r:
            output.append(TextNode(node.text[l:r], TextType.TEXT))

    print ("output: ", output)    
    return output