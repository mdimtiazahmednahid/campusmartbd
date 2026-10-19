import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

match = re.search(r'\.btn-shop-now\s*\{[^\}]*\}', css)
if match:
    print(match.group(0))
