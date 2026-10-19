import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Replace the black background with blue background in promo-container
old_bg = r'''    /* Premium Black background */
    background: linear-gradient(135deg, #18181b 0%, #000000 100%);'''
new_bg = r'''    /* Premium Blue background matching logo */
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);'''
css = css.replace(old_bg, new_bg)

# Replace the title color from orange to white so it's readable on blue
old_title_color = r'''    color: #f97316; /* Orange text */'''
new_title_color = r'''    color: #ffffff; /* White text */'''
css = css.replace(old_title_color, new_title_color)

# Replace the box shadow to match blue
old_shadow = r'''box-shadow: 0 20px 50px rgba(0,0,0,0.5);'''
new_shadow = r'''box-shadow: 0 20px 40px rgba(37, 99, 235, 0.3);'''
css = css.replace(old_shadow, new_shadow)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Updated background to blue")
