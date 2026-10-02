from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', 'path', 'rect', 'svg'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.stack:
            print(f"Error: Unmatched closing tag </{tag}>")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
        else:
            print(f"Error: Mismatched closing tag. Expected </{self.stack[-1]}>, got </{tag}>")
            self.stack.pop()

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

parser = MyHTMLParser()
parser.feed(html)
if parser.stack:
    print(f"Error: Unclosed tags remaining: {parser.stack}")
else:
    print("HTML is perfectly balanced!")
