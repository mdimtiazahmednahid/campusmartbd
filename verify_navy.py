import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Let's extract the promo-container block
match = re.search(r'\.promo-container\s*\{([^\}]+)\}', css)
if match:
    print(match.group(1))
