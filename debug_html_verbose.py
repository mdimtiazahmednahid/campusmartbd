from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', 'path', 'rect', 'svg'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            attrs_dict = dict(attrs)
            class_name = attrs_dict.get('class', attrs_dict.get('id', ''))
            self.stack.append((tag, class_name, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.stack:
            return
        last_tag, class_name, pos = self.stack[-1]
        if last_tag == tag:
            self.stack.pop()
        else:
            pass # we'll print it out at the end

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

parser = MyHTMLParser()
parser.feed(html)
for item in parser.stack:
    print(item)
