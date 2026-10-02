import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

def repl(match):
    size_id = match.group(1)
    # the match contains the whole size-selector div
    # we'll replace it with a container holding all three
    new_html = f'''<div class="options-row" style="display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center; width: 100%;">
                                    <div class="size-selector" style="flex: 1; min-width: 30%;">
                                        <select id="{size_id}" class="size-select" style="width: 100%; font-size: 0.85rem;" aria-label="Size">
                                            <option value="" disabled selected>Size</option>
                                            <option value="M">M</option>
                                            <option value="L">L</option>
                                            <option value="XL">XL</option>
                                            <option value="XXL">XXL</option>
                                            <option value="3XL">3XL</option>
                                        </select>
                                    </div>
                                    <div class="size-selector" style="flex: 1; min-width: 30%;">
                                        <select id="collar-{size_id.split('-')[1]}" class="collar-select size-select" style="width: 100%; font-size: 0.85rem;" aria-label="Collar">
                                            <option value="" disabled selected>Collar</option>
                                            <option value="Polo">Polo</option>
                                            <option value="Round">Round</option>
                                        </select>
                                    </div>
                                    <div class="size-selector" style="flex: 1; min-width: 30%;">
                                        <select id="sleeve-{size_id.split('-')[1]}" class="sleeve-select size-select" style="width: 100%; font-size: 0.85rem;" aria-label="Sleeve">
                                            <option value="" disabled selected>Sleeve</option>
                                            <option value="Half">Half</option>
                                            <option value="Full">Full</option>
                                        </select>
                                    </div>
                                </div>'''
    return new_html

# regex to find the size-selector div
pattern = r'<div class="size-selector">\s*<label for="(size-\d+)">Size:</label>\s*<select id="\1" class="size-select">\s*<option value="M">M</option>\s*<option value="L">L</option>\s*<option value="XL">XL</option>\s*<option value="XXL">XXL</option>\s*<option value="3XL">3XL</option>\s*</select>\s*</div>'

new_html = re.sub(pattern, repl, html)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(new_html)

print("Updated HTML")
