import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# Replace lines 207-210
old1 = r'''            const collar = item\.collar \|\| 'Not Selected';
            const sleeve = item\.sleeve \|\| 'Not Selected';
            orderDetailsStr \+= `\$\{item\.title\} \(\$\{collar\}, \$\{sleeve\}, Size: \$\{item\.size\}\) x\$\{item\.quantity\} - ৳\$\{effectivePrice \* item\.quantity\}
`;'''
new1 = r'''            const tShirtType = item.tShirtType || 'Not Selected';
            const sizeMap = {
                'M': 'M (Chest-38, Length-27)',
                'L': 'L (Chest-40, Length-28)',
                'XL': 'XL (Chest-42, Length-29)',
                'XXL': 'XXL (Chest-44, Length-30)',
                '3XL': '3XL (Chest-46, Length-31)'
            };
            const detailedSize = sizeMap[item.size] || item.size;
            orderDetailsStr += `${item.title} (${tShirtType}, Size: ${detailedSize}) x${item.quantity} - ৳${effectivePrice * item.quantity}\n`;'''
js = re.sub(old1, new1, js)

# Replace line 218
old2 = r'<div class="cart-item-meta">\$\{item\.collar \|\| "Not Selected"\}, \$\{item\.sleeve \|\| "Not Selected"\}, Size: \$\{item\.size\}</div>'
new2 = r'<div class="cart-item-meta">${item.tShirtType || "Not Selected"}, Size: ${item.size}</div>'
js = re.sub(old2, new2, js)

# Replace lines 336-353
old3 = r'''        const collarSelect = document\.getElementById\(`collar-\$\{id\}`\);
        const sleeveSelect = document\.getElementById\(`sleeve-\$\{id\}`\);
        
        const size = sizeSelect \? sizeSelect\.value : '';
        const collar = collarSelect \? collarSelect\.value : '';
        const sleeve = sleeveSelect \? sleeveSelect\.value : '';

        if \(!size \|\| !collar \|\| !sleeve\) \{
            alert\('Please select a Size, Collar type, and Sleeve type before adding to cart.'\);
            return;
        \}

        const existingItemIndex = cart\.findIndex\(item => item\.id === id && item\.size === size && item\.collar === collar && item\.sleeve === sleeve\);
        
        if \(existingItemIndex > -1\) \{
            cart\[existingItemIndex\]\.quantity\+\+;
        \} else \{
            cart\.push\(\{ id, title, price, image, size, collar, sleeve, quantity: 1 \}\);
        \}'''

new3 = r'''        const typeSelect = document.getElementById(`type-${id}`);
        
        const size = sizeSelect ? sizeSelect.value : '';
        const tShirtType = typeSelect ? typeSelect.value : '';

        if (!size || !tShirtType) {
            alert('Please select a Size and T-shirt Type before adding to cart.');
            return;
        }

        const existingItemIndex = cart.findIndex(item => item.id === id && item.size === size && item.tShirtType === tShirtType);
        
        if (existingItemIndex > -1) {
            cart[existingItemIndex].quantity++;
        } else {
            cart.push({ id, title, price, image, size, tShirtType, quantity: 1 });
        }'''
js = re.sub(old3, new3, js)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Updated script.js fully")
