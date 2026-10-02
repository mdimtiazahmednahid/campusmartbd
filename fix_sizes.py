import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Replace all <option value="M">M</option> with <option value="M">M (Chest-38, Length-27)</option>
html = html.replace('<option value="M">M</option>', '<option value="M">M (Chest-38, Length-27)</option>')
html = html.replace('<option value="L">L</option>', '<option value="L">L (Chest-40, Length-28)</option>')
html = html.replace('<option value="XL">XL</option>', '<option value="XL">XL (Chest-42, Length-29)</option>')
html = html.replace('<option value="XXL">XXL</option>', '<option value="XXL">XXL (Chest-44, Length-30)</option>')
html = html.replace('<option value="3XL">3XL</option>', '<option value="3XL">3XL (Chest-46, Length-31)</option>')

# Ensure the flex containers don't break by setting min-width: 0
html = html.replace('style="flex: 1; min-width: 30%;"', 'style="flex: 1; min-width: 0;"')

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)


with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

old_css = r'''\.size-select\s*\{
    padding: 0\.25rem 0\.5rem;
    border: 1px solid var\(--border-color\);
    border-radius: 4px;
    font-family: inherit;
    outline: none;
    cursor: pointer;
\}'''

new_css = r'''.size-select {
    padding: 0.25rem 0.5rem;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    font-family: inherit;
    outline: none;
    cursor: pointer;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 100%;
}'''

match = re.search(old_css, css)
if match:
    css = css.replace(match.group(0), new_css)
else:
    css += '\n' + new_css

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Updated sizes and CSS")
