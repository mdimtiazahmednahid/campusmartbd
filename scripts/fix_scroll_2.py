import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

old_style = 'style="flex: 1; overflow-y: auto; overflow-x: hidden; margin: 0; padding: 0;"'
new_style = 'style="flex: 1; overflow-y: auto; overflow-x: hidden; margin: 0; padding: 0; max-height: calc(100vh - 70px); -webkit-overflow-scrolling: touch;"'

html = html.replace(old_style, new_style)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)
print("Added touch scrolling and height max constraints")
