import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

match = re.search(r'\.size-select\s*\{[^\}]*\}', css)
if match:
    print(match.group(0))
else:
    print("No .size-select found in style.css")
