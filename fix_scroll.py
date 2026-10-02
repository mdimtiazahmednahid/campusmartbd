with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Add flex-shrink: 0 to cart-footer if not there
if "flex-shrink: 0;" not in css.split(".cart-footer {")[1].split("}")[0]:
    css = css.replace('.cart-footer {\n    padding: 1.5rem 1.5rem 3rem 1.5rem;\n    border-top: 1px solid var(--border-color);\n    background: var(--section-bg);\n}',
                      '.cart-footer {\n    padding: 1.5rem 1.5rem 3rem 1.5rem;\n    border-top: 1px solid var(--border-color);\n    background: var(--section-bg);\n    flex-shrink: 0;\n}')

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Fixed flex-shrink")
