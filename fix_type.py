import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

for i in range(1, 7):
    pattern = r'(<div class="size-selector" style="flex: 1; min-width: 0;">\s*<select id="collar-' + str(i) + r'".*?</select>\s*</div>\s*<div class="size-selector" style="flex: 1; min-width: 0;">\s*<select id="sleeve-' + str(i) + r'".*?</select>\s*</div>)'
    replacement = f'''<div class="size-selector" style="flex: 2; min-width: 0;">
                                        <select id="type-{i}" class="type-select size-select"
                                            style="width: 100%; font-size: 0.85rem;" aria-label="T-shirt Type">
                                            <option value="" disabled selected>Type</option>
                                            <option value="Polo Collar + half sleeve">Polo Collar + half sleeve</option>
                                            <option value="Polo Collar + full sleeve">Polo Collar + full sleeve</option>
                                            <option value="Round Collar + half sleeve">Round Collar + half sleeve</option>
                                            <option value="Round Collar + full sleeve">Round Collar + full sleeve</option>
                                        </select>
                                    </div>'''
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)

print("Updated HTML with combined T-shirt Type dropdown")
