with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# Fix the broken image
js = js.replace("'assets/sustverse-white.png'", "'assets/sust-blue.png'")

# Fix XXL/3XL pricing
js = js.replace("if (sizeSelect && sizeSelect.value === 'XXL')", "if (sizeSelect && (sizeSelect.value === 'XXL' || sizeSelect.value === '3XL'))")

# Safely inject size mapping before orderDetailsStr
target_line = "            orderDetailsStr += `${item.title} (${collar}, ${sleeve}, Size: ${item.size}) x${item.quantity} - ৳${effectivePrice * item.quantity}\\n`;"
replacement = """            const sizeMap = {
                'M': 'M (Chest-38, Length-27)',
                'L': 'L (Chest-40, Length-28)',
                'XL': 'XL (Chest-42, Length-29)',
                'XXL': 'XXL (Chest-44, Length-30)',
                '3XL': '3XL (Chest-46, Length-31)'
            };
            const detailedSize = sizeMap[item.size] || item.size;
            orderDetailsStr += `${item.title} (${collar}, ${sleeve}, Size: ${detailedSize}) x${item.quantity} - ৳${effectivePrice * item.quantity}\\n`;"""

js = js.replace(target_line, replacement)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Safely updated script.js")
