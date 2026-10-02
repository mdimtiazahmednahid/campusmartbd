import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# I will find the cart-sidebar block and completely replace it with the reordered version.
pattern = r'<!-- Cart Modal / Sidebar -->.*?<div class="toast"'
match = re.search(pattern, html, flags=re.DOTALL)

if not match:
    print("Could not find cart sidebar block")
    exit(1)

old_sidebar = match.group(0)

# We will construct a new sidebar manually, preserving the exact form inputs so we don't break anything.
# Let's extract the form inputs from the old sidebar.

def extract_section(section_name):
    # This is a bit risky if HTML changes, but I can extract the specific divs.
    pass

# Actually, it's safer to just read the whole file and do a multi-line replacement of the structure.
