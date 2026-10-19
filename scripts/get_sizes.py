import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Try to find a size guide table or section
match = re.search(r'Size Guide.*?</table>', html, re.DOTALL | re.IGNORECASE)
if match:
    print("Found size guide:")
    print(match.group(0))
else:
    # Just print any mentions of "Chest" or "Length"
    matches = re.findall(r'.{0,30}Chest.{0,30}', html, re.IGNORECASE)
    print("Chest mentions:")
    for m in matches:
        print(m)
