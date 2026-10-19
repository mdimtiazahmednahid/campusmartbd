import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Grab the options row for product 1 to see the structure
match = re.search(r'<div class="options-row"[^>]*>.*?</div>\s*</div>', html, re.DOTALL)
if match:
    print(match.group(0))
