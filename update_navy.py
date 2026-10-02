import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Replace the blue background with premium navy blue
old_bg = r'''    /* Premium Blue background matching logo */
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);'''
new_bg = r'''    /* Premium Navy Blue background */
    background: linear-gradient(135deg, #070f2b 0%, #1b1a55 100%);'''
css = css.replace(old_bg, new_bg)

# Alternatively try regex if the exact string wasn't matched
if "Premium Navy Blue" not in css:
    css = re.sub(r'background:\s*linear-gradient\([^;]+\);\s*/\* Premium (Blue|Black) background.*?\*/', 
                 r'/* Premium Navy Blue */\n    background: linear-gradient(135deg, #060d23 0%, #101c40 100%);', css)
    # let's just do a simpler replace
    css = re.sub(r'background: linear-gradient\(135deg, #[0-9a-f]+ 0%, #[0-9a-f]+ 100%\);',
                 r'background: linear-gradient(135deg, #0a1128 0%, #152243 100%);', css, count=1)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Updated to Navy Blue")
