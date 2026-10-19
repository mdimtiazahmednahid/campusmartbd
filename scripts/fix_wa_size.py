import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_logic = '''            waMsg += `\\n*Order Summary:*\\n`;
            let imageUrls = [];
            cart.forEach(item => {
                waMsg += `- ${item.title} (${item.tShirtType || 'N/A'}, Size: ${item.size || 'N/A'}) x${item.quantity}\\n`;
                if (item.image) {'''

new_logic = '''            waMsg += `\\n*Order Summary:*\\n`;
            let imageUrls = [];
            cart.forEach(item => {
                const sizeMap = {
                    'M': 'M (Chest-38, Length-27)',
                    'L': 'L (Chest-40, Length-28)',
                    'XL': 'XL (Chest-42, Length-29)',
                    'XXL': 'XXL (Chest-44, Length-30)',
                    '3XL': '3XL (Chest-46, Length-31)'
                };
                const fullSize = sizeMap[item.size] || item.size || 'N/A';
                waMsg += `- ${item.title} (${item.tShirtType || 'N/A'}, Size: ${fullSize}) x${item.quantity}\\n`;
                if (item.image) {'''

js = js.replace(old_logic, new_logic)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Added sizeMap to WhatsApp payload")
