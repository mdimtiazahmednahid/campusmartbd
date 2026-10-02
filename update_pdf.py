import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# Expand size measurements in the order details string
old_order = r'''const collar = item.collar || 'Not Selected';
            const sleeve = item.sleeve || 'Not Selected';
            orderDetailsStr \+= `\$\{item\.title\} \(\$\{collar\}, \$\{sleeve\}, Size: \$\{item\.size\}\) x\$\{item\.quantity\} - ৳\$\{effectivePrice \* item\.quantity\}\\n`;'''

new_order = r'''const collar = item.collar || 'Not Selected';
            const sleeve = item.sleeve || 'Not Selected';
            
            // Map sizes to their detailed string
            const sizeMap = {
                'M': 'M (Chest-38, Length-27)',
                'L': 'L (Chest-40, Length-28)',
                'XL': 'XL (Chest-42, Length-29)',
                'XXL': 'XXL (Chest-44, Length-30)',
                '3XL': '3XL (Chest-46, Length-31)'
            };
            const detailedSize = sizeMap[item.size] || item.size;
            
            orderDetailsStr += `${item.title} (${collar}, ${sleeve}, Size: ${detailedSize}) x${item.quantity} - ৳${effectivePrice * item.quantity}\n`;'''

js = re.sub(old_order, new_order, js)

# Also check XXL and 3XL pricing logic to ensure 3XL gets charged 50 BDT as well
old_pricing = r'''            if \(sizeSelect && sizeSelect\.value === 'XXL'\) \{
                additionalCost = 50;
            \}'''

new_pricing = r'''            if (sizeSelect && (sizeSelect.value === 'XXL' || sizeSelect.value === '3XL')) {
                additionalCost = 50;
            }'''
            
js = re.sub(old_pricing, new_pricing, js)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Updated size mapping and pricing logic")
