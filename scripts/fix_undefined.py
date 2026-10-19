import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# Fix orderDetailsStr
old_order = r'orderDetailsStr \+= `\$\{item\.title\} \(\$\{item\.collar\}, \$\{item\.sleeve\}, Size: \$\{item\.size\}\) x\$\{item\.quantity\} - ৳\$\{effectivePrice \* item\.quantity\}\\n`;'
new_order = r'''const collar = item.collar || 'Not Selected';
            const sleeve = item.sleeve || 'Not Selected';
            orderDetailsStr += `${item.title} (${collar}, ${sleeve}, Size: ${item.size}) x${item.quantity} - ৳${effectivePrice * item.quantity}\n`;'''
js = re.sub(old_order, new_order, js)

# Fix cart-item-meta
old_meta = r'<div class="cart-item-meta">\$\{item\.collar\}, \$\{item\.sleeve\}, Size: \$\{item\.size\}</div>'
new_meta = r'<div class="cart-item-meta">${item.collar || "Not Selected"}, ${item.sleeve || "Not Selected"}, Size: ${item.size}</div>'
js = re.sub(old_meta, new_meta, js)

# Fix address in PDF
old_address = r"const address = `\$\{formData\.get\('address'\)\}, \$\{formData\.get\('upazila'\)\}, \$\{formData\.get\('district'\)\}, \$\{formData\.get\('division'\)\}`;"
new_address = r"const address = `${formData.get('address') || ''}, ${formData.get('upazila') || ''}, ${formData.get('district') || ''}, ${formData.get('division') || ''}`;"
js = re.sub(old_address, new_address, js)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Fixed undefined variables")
