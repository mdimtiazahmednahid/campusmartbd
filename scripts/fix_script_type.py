import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# Update validation block
old_validation = r'''        const sizeSelect = document.getElementById(`size-${id}`);
        const collarSelect = document.getElementById(`collar-${id}`);
        const sleeveSelect = document.getElementById(`sleeve-${id}`);
        
        const size = sizeSelect \? sizeSelect.value : '';
        const collar = collarSelect \? collarSelect.value : '';
        const sleeve = sleeveSelect \? sleeveSelect.value : '';

        if \(!size \|\| !collar \|\| !sleeve\) \{
            alert\('Please select a Size, Collar type, and Sleeve type before adding to cart.'\);
            return;
        \}'''

new_validation = r'''        const sizeSelect = document.getElementById(`size-${id}`);
        const typeSelect = document.getElementById(`type-${id}`);
        
        const size = sizeSelect ? sizeSelect.value : '';
        const tShirtType = typeSelect ? typeSelect.value : '';

        if (!size || !tShirtType) {
            alert('Please select a Size and T-shirt Type before adding to cart.');
            return;
        }'''

js = re.sub(old_validation, new_validation, js)

# Update Add to Cart block
old_cart_add = r'''        // Add item to cart
        const existingItem = cart.find\(item => item.id === id && item.size === size && item.collar === collar && item.sleeve === sleeve\);
        if \(existingItem\) \{
            existingItem.quantity \+= 1;
        \} else \{
            cart.push\(\{ id, title, price, image, size, collar, sleeve, quantity: 1 \}\);
        \}'''

new_cart_add = r'''        // Add item to cart
        const existingItem = cart.find(item => item.id === id && item.size === size && item.tShirtType === tShirtType);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({ id, title, price, image, size, tShirtType, quantity: 1 });
        }'''

js = re.sub(old_cart_add, new_cart_add, js)

# Update Cart UI and Order String
old_order_str = r'''            const collar = item.collar \|\| 'Not Selected';
            const sleeve = item.sleeve \|\| 'Not Selected';
            
            // Map sizes to their detailed string
            const sizeMap = \{
                'M': 'M \(Chest-38, Length-27\)',
                'L': 'L \(Chest-40, Length-28\)',
                'XL': 'XL \(Chest-42, Length-29\)',
                'XXL': 'XXL \(Chest-44, Length-30\)',
                '3XL': '3XL \(Chest-46, Length-31\)'
            \};
            const detailedSize = sizeMap\[item.size\] \|\| item.size;
            orderDetailsStr \+= `\$\{item.title\} \(\$\{collar\}, \$\{sleeve\}, Size: \$\{detailedSize\}\) x\$\{item.quantity\} - ৳\$\{effectivePrice \* item.quantity\}\\n`;'''

new_order_str = r'''            const tShirtType = item.tShirtType || 'Not Selected';
            
            // Map sizes to their detailed string
            const sizeMap = {
                'M': 'M (Chest-38, Length-27)',
                'L': 'L (Chest-40, Length-28)',
                'XL': 'XL (Chest-42, Length-29)',
                'XXL': 'XXL (Chest-44, Length-30)',
                '3XL': '3XL (Chest-46, Length-31)'
            };
            const detailedSize = sizeMap[item.size] || item.size;
            orderDetailsStr += `${item.title} (${tShirtType}, Size: ${detailedSize}) x${item.quantity} - ৳${effectivePrice * item.quantity}\n`;'''

js = re.sub(old_order_str, new_order_str, js)

old_cart_item = r'''                <div class="cart-item-details">
                    <h4>\$\{item.title\}</h4>
                    <p>\$\{collar\} • \$\{sleeve\} • Size: \$\{item.size\}</p>
                    <p class="cart-item-price">৳\$\{effectivePrice\}</p>'''

new_cart_item = r'''                <div class="cart-item-details">
                    <h4>${item.title}</h4>
                    <p>${item.tShirtType} • Size: ${item.size}</p>
                    <p class="cart-item-price">৳${effectivePrice}</p>'''

js = re.sub(old_cart_item, new_cart_item, js)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Updated script.js to use tShirtType")
