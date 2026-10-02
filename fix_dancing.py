import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

old_wrapper_mobile = '''    .promo-image-wrapper {
        height: 260px; /* Slightly taller for better view */
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }'''

new_wrapper_mobile = '''    .promo-image-wrapper {
        height: 260px; /* Strictly defined */
        min-height: 260px;
        flex: none; /* Do not allow flex layout to squash it */
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden; /* Prevent jumping */
    }'''

css = css.replace(old_wrapper_mobile, new_wrapper_mobile)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)
print("Fixed wrapper height")
