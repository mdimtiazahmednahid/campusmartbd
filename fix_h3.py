import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Replace any h3 in the footer so it's fully visible (we already applied this, just double-checking)
if '.footer-links h3, .footer-contact h3, .footer-social h3 {' in css:
    print("Already applied h3 color fix")
else:
    css = re.sub(
        r'(\.footer-links h3, \.footer-contact h3, \.footer-social h3 \{[^}]*)\}',
        r'\1\n    color: white;\n}',
        css
    )
    with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
        f.write(css)
    print("Fixed h3 color")
