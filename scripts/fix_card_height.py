import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

old_block = '''.product-image-container {
    background: #ffffff !important; /* Pure White as requested */
    border-radius: 16px !important;
    position: relative;
    padding: 1.5rem;
}'''

new_block = '''.product-image-container {
    background: #ffffff !important; /* Pure White as requested */
    border-radius: 16px !important;
    position: relative;
    padding: 1rem !important;
    aspect-ratio: 1 / 1 !important;
    margin-bottom: 1rem !important;
}'''

css = css.replace(old_block, new_block)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)
print("Fixed card height")
