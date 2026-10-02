import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# 1. Update updateCart rendering
js = re.sub(
    r'(orderDetailsStr \+= `\$\{item\.title\} \(Size: \$\{item\.size\}\) x\$\{item\.quantity\} - ৳\$\{effectivePrice \* item\.quantity\}\\n`;)',
    r'orderDetailsStr += `${item.title} (${item.collar}, ${item.sleeve}, Size: ${item.size}) x${item.quantity} - ৳${effectivePrice * item.quantity}\\n`;',
    js
)

js = re.sub(
    r'(<div class="cart-item-meta">Size: \$\{item\.size\}</div>)',
    r'<div class="cart-item-meta">${item.collar}, ${item.sleeve}, Size: ${item.size}</div>',
    js
)

# 2. Update dynamic pricing
dynamic_pricing_old = r'''    document\.querySelectorAll\('\.size-select'\)\.forEach\(select => \{
        select\.addEventListener\('change', \(e\) => \{
            const card = e\.target\.closest\('\.product-card'\);
            const priceElement = card\.querySelector\('\.current-price'\);
            const addBtn = card\.querySelector\('\.btn-add-cart'\);
            const buyBtn = card\.querySelector\('\.btn-buy-now'\);
            
            // Assuming base price is what is initially set, let's read it or assume 450 for Kiloroad, 400 for Red Sustverse
            // Better to pull from data attribute\. If not set, initialize it\.
            if \(!card\.dataset\.basePrice\) \{
                card\.dataset\.basePrice = addBtn\.getAttribute\('data-price'\);
            \}
            
            let basePrice = parseInt\(card\.dataset\.basePrice\);
            let additionalCost = 0;
            
            // Add 50 BDT for XXL size
            if \(e\.target\.value === 'XXL'\) \{
                additionalCost = 50;
            \}
            
            const newPrice = basePrice \+ additionalCost;
            
            // Update UI and Button data attributes
            priceElement\.textContent = `৳ \$\{newPrice\}`;
            addBtn\.setAttribute\('data-price', newPrice\);
            buyBtn\.setAttribute\('data-price', newPrice\);
        \}\);
    \}\);'''

dynamic_pricing_new = r'''    document.querySelectorAll('.size-select').forEach(select => {
        select.addEventListener('change', (e) => {
            const card = e.target.closest('.product-card');
            const priceElement = card.querySelector('.current-price');
            const addBtn = card.querySelector('.btn-add-cart');
            const buyBtn = card.querySelector('.btn-buy-now');
            
            const id = addBtn.getAttribute('data-id');
            const sizeSelect = document.getElementById(`size-${id}`);
            
            if (!card.dataset.basePrice) {
                card.dataset.basePrice = addBtn.getAttribute('data-price');
            }
            
            let basePrice = parseInt(card.dataset.basePrice);
            let additionalCost = 0;
            
            if (sizeSelect && sizeSelect.value === 'XXL') {
                additionalCost = 50;
            }
            
            const newPrice = basePrice + additionalCost;
            
            priceElement.textContent = `৳ ${newPrice}`;
            addBtn.setAttribute('data-price', newPrice);
            buyBtn.setAttribute('data-price', newPrice);
        });
    });'''

js = re.sub(dynamic_pricing_old, dynamic_pricing_new, js)

# 3. Update handleAddToCart
add_to_cart_old = r'''    const handleAddToCart = \(btn, openAfter = false\) => \{
        const id = btn\.getAttribute\('data-id'\);
        const title = btn\.getAttribute\('data-title'\);
        const price = parseInt\(btn\.getAttribute\('data-price'\)\);
        const image = btn\.getAttribute\('data-image'\);
        
        // Get size
        const sizeSelect = document\.getElementById\(`size-\$\{id\}`\);
        const size = sizeSelect \? sizeSelect\.value : 'M';

        // Check if item already exists in cart with same size
        const existingItemIndex = cart\.findIndex\(item => item\.id === id && item\.size === size\);
        
        if \(existingItemIndex > -1\) \{
            cart\[existingItemIndex\]\.quantity\+\+;
        \} else \{
            cart\.push\(\{ id, title, price, image, size, quantity: 1 \}\);
        \}'''

add_to_cart_new = r'''    const handleAddToCart = (btn, openAfter = false) => {
        const id = btn.getAttribute('data-id');
        const title = btn.getAttribute('data-title');
        const price = parseInt(btn.getAttribute('data-price'));
        const image = btn.getAttribute('data-image');
        
        const sizeSelect = document.getElementById(`size-${id}`);
        const collarSelect = document.getElementById(`collar-${id}`);
        const sleeveSelect = document.getElementById(`sleeve-${id}`);
        
        const size = sizeSelect ? sizeSelect.value : '';
        const collar = collarSelect ? collarSelect.value : '';
        const sleeve = sleeveSelect ? sleeveSelect.value : '';

        if (!size || !collar || !sleeve) {
            alert('Please select a Size, Collar type, and Sleeve type before adding to cart.');
            return;
        }

        const existingItemIndex = cart.findIndex(item => item.id === id && item.size === size && item.collar === collar && item.sleeve === sleeve);
        
        if (existingItemIndex > -1) {
            cart[existingItemIndex].quantity++;
        } else {
            cart.push({ id, title, price, image, size, collar, sleeve, quantity: 1 });
        }'''

js = re.sub(add_to_cart_old, add_to_cart_new, js)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Updated script.js")
