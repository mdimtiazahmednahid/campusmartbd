import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

old_css = '''.delivery-card-label input {
    display: none; /* Hide standard radio */
}'''

new_css = '''.delivery-card-label input {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
    margin: 0;
    padding: 0;
}'''

css = css.replace(old_css, new_css)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)
print("Fixed radio button CSS visibility bug for mobile")
