import re

# Update script.js to fix broken image link
with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

js = js.replace("'assets/sustverse-white.png',", "'assets/sust-blue.png',")

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

# Update style.css
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Make the card bigger
css = css.replace("max-width: 800px;", "max-width: 900px;")

# Change background to premium red
old_bg = r"background: linear-gradient\(135deg, #070f2b 0%, #1b1a55 100%\);"
new_bg = r"background: linear-gradient(135deg, #991b1b 0%, #450a0a 100%); /* Premium Dark Red */"
css = re.sub(old_bg, new_bg, css)

# Make orange text white (so it looks good on red)
css = css.replace("color: #f97316; /* Orange text */", "color: #ffffff; /* White text */")
css = css.replace("background: linear-gradient(to bottom, #ea580c, #f97316); /* Orange accent on left */", "background: linear-gradient(to bottom, #ffffff, #facc15); /* White/Yellow accent */")

# The button is currently orange. Yellow or white would look better on dark red
old_btn = r"background: linear-gradient\(to right, #ea580c, #f97316\); /\* Orange button \*/\n\s*color: white;"
new_btn = r"background: linear-gradient(to right, #ffffff, #f3f4f6); /* White button */\n    color: #991b1b;"
css = re.sub(old_btn, new_btn, css)

# Make image wrapper larger on desktop
css = css.replace("height: 180px;", "height: 240px;")

# Mobile overrides
old_mob_wrapper = r"height: 140px;\n\s*flex: 0.8;"
new_mob_wrapper = r"height: 180px;\n        flex: 1;"
css = re.sub(old_mob_wrapper, new_mob_wrapper, css)

# Fix mobile button text color if we changed it globally
css = css.replace("color: white;\n    font-weight: 700;\n    font-size: 1rem;\n    padding: 0.75rem 2rem;\n    border-radius: 50px;\n    box-shadow: 0 4px 15px rgba(234, 88, 12, 0.4);", 
                  "color: #991b1b;\n    font-weight: 800;\n    font-size: 1rem;\n    padding: 0.75rem 2rem;\n    border-radius: 50px;\n    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);")

css = css.replace("box-shadow: 0 6px 20px rgba(234, 88, 12, 0.6);\n    color: white;", "box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);\n    color: #7f1d1d;")

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Updated to Red background and fixed image")
