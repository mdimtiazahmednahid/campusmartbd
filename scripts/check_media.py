import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

match = re.search(r'@media \(max-width: 768px\) \{.*?(?=\s*@media|\Z)', css, re.DOTALL)
if match:
    print(match.group(0))
