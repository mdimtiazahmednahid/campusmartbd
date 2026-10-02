import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Pattern to remove the product-options div inside product cards
# It looks like:
# <div class="product-options"> ... </div>
# between <div class="product-info"> and <div class="product-actions">

pattern = r'<div class="product-options">.*?</div>\s*(<div class="product-actions">)'
html = re.sub(pattern, r'\1', html, flags=re.DOTALL)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)
print("Removed product options")
