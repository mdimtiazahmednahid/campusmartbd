from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', 'path', 'rect', 'svg'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.stack:
            print(f"Error: Unmatched closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack[-1]
        if last_tag == tag:
            self.stack.pop()
        else:
            print(f"Error at line {self.getpos()[0]}: Mismatched closing tag. Expected </{last_tag}> (opened at {pos}), got </{tag}>")
            self.stack.pop()

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

parser = MyHTMLParser()
parser.feed(html)
