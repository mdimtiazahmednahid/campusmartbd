import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Let's simplify the form inline styles.
# Old: style="display: flex; flex-direction: column; flex: 1; overflow: hidden; margin: 0; padding: 0; min-height: 0;"
# New: style="flex: 1; overflow-y: auto; margin: 0; padding: 0; display: block;"

old_style = 'style="display: flex; flex-direction: column; flex: 1; overflow: hidden; margin: 0; padding: 0; min-height: 0;"'
new_style = 'style="flex: 1; overflow-y: auto; overflow-x: hidden; margin: 0; padding: 0;"'

html = html.replace(old_style, new_style)

# Also remove the flex properties from cart-scrollable-content so it just acts as a normal div
old_scroll_content = 'class="cart-scrollable-content" style="flex: 1; overflow-y: auto; padding: 1.5rem;"'
new_scroll_content = 'class="cart-scrollable-content" style="padding: 1.5rem;"'
html = html.replace(old_scroll_content, new_scroll_content)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)
print("Simplified scrolling")
