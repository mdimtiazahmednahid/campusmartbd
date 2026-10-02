import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# 1. Update Add to Cart buttons
old_add_cart = r'''        const sizeSelect = document.getElementById(`size-${id}`);
        const typeSelect = document.getElementById(`type-${id}`);
        
        const size = sizeSelect ? sizeSelect.value : '';
        const tShirtType = typeSelect ? typeSelect.value : '';

        if (!size || !tShirtType) {
            showToast('Please select a Size and T-shirt Type before adding to cart.'); reportError('Missing size/type selection', 'add_to_cart');
            return;
        }

        const existingItemIndex = cart.findIndex(item => item.id === id && item.size === size && item.tShirtType === tShirtType);
        
        if (existingItemIndex > -1) {
            cart[existingItemIndex].quantity++;
        } else {
            cart.push({ id, title, price, image, size, tShirtType, quantity: 1 });
        }'''

new_add_cart = r'''        // Now, items are added directly to the cart without initial size/type.
        // If an identical item (same id, same empty size/type) exists, increment qty.
        const size = '';
        const tShirtType = '';

        const existingItemIndex = cart.findIndex(item => item.id === id && item.size === size && item.tShirtType === tShirtType);
        
        if (existingItemIndex > -1) {
            cart[existingItemIndex].quantity++;
        } else {
            cart.push({ id, title, price, image, size, tShirtType, quantity: 1 });
        }'''

if old_add_cart in js:
    js = js.replace(old_add_cart, new_add_cart)
else:
    print("Could not find old add cart")

# 2. Update cart item rendering
old_cart_render = r'''            const itemEl = document.createElement('div');
            itemEl.className = 'cart-item';
            itemEl.innerHTML = `
                <img src="${item.image}" alt="${item.title}">
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.title}</div>
                    <div class="cart-item-meta">${item.tShirtType || "Not Selected"}, Size: ${item.size}</div>
                    <div class="cart-item-price">৳ ${effectivePrice} ${isEarlyBirds ? '<del style="font-size:0.75rem;color:#9ca3af;margin-left:0.25rem;">৳ '+item.price+'</del>' : ''}</div>
                    <div class="cart-item-actions">
                        <button class="qty-btn minus" data-index="${index}">-</button>
                        <span>${item.quantity}</span>
                        <button class="qty-btn plus" data-index="${index}">+</button>
                        <button class="remove-item" data-index="${index}">Remove</button>
                    </div>
                </div>
            `;
            cartItemsContainer.appendChild(itemEl);'''

new_cart_render = r'''            const itemEl = document.createElement('div');
            itemEl.className = 'cart-item';
            
            itemEl.innerHTML = `
                <img src="${item.image}" alt="${item.title}">
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.title}</div>
                    <div class="cart-item-options" style="display:flex; gap:0.5rem; margin-top:0.25rem;">
                        <select class="cart-size-select" data-index="${index}" style="padding:0.25rem; font-size:0.8rem; border-radius:4px; border:1px solid var(--border-color); width:48%; background:white; cursor:pointer; outline:none; ${(item.size === '' && document.getElementById('checkout-form').classList.contains('submitted')) ? 'border-color: #dc2626; box-shadow: 0 0 0 1px #dc2626;' : ''}">
                            <option value="">Size</option>
                            <option value="M" ${item.size === 'M' ? 'selected' : ''}>M</option>
                            <option value="L" ${item.size === 'L' ? 'selected' : ''}>L</option>
                            <option value="XL" ${item.size === 'XL' ? 'selected' : ''}>XL</option>
                            <option value="XXL" ${item.size === 'XXL' ? 'selected' : ''}>XXL</option>
                            <option value="3XL" ${item.size === '3XL' ? 'selected' : ''}>3XL</option>
                        </select>
                        <select class="cart-type-select" data-index="${index}" style="padding:0.25rem; font-size:0.8rem; border-radius:4px; border:1px solid var(--border-color); width:48%; background:white; cursor:pointer; outline:none; ${(item.tShirtType === '' && document.getElementById('checkout-form').classList.contains('submitted')) ? 'border-color: #dc2626; box-shadow: 0 0 0 1px #dc2626;' : ''}">
                            <option value="">Type</option>
                            <option value="Polo Collar + half sleeve" ${item.tShirtType === 'Polo Collar + half sleeve' ? 'selected' : ''}>Polo + Half</option>
                            <option value="Polo Collar + full sleeve" ${item.tShirtType === 'Polo Collar + full sleeve' ? 'selected' : ''}>Polo + Full</option>
                            <option value="Round Collar + half sleeve" ${item.tShirtType === 'Round Collar + half sleeve' ? 'selected' : ''}>Round + Half</option>
                            <option value="Round Collar + full sleeve" ${item.tShirtType === 'Round Collar + full sleeve' ? 'selected' : ''}>Round + Full</option>
                        </select>
                    </div>
                    <div class="cart-item-price" style="margin-top:0.5rem;">৳ ${effectivePrice} ${isEarlyBirds ? '<del style="font-size:0.75rem;color:#9ca3af;margin-left:0.25rem;">৳ '+item.price+'</del>' : ''}</div>
                    <div class="cart-item-actions">
                        <button class="qty-btn minus" data-index="${index}">-</button>
                        <span>${item.quantity}</span>
                        <button class="qty-btn plus" data-index="${index}">+</button>
                        <button class="remove-item" data-index="${index}">Remove</button>
                    </div>
                </div>
            `;
            cartItemsContainer.appendChild(itemEl);'''

if old_cart_render in js:
    js = js.replace(old_cart_render, new_cart_render)
else:
    print("Could not find old cart render")


# 3. Add event listeners to the new dropdowns right after they are created
old_btn_listeners = r'''        // Add event listeners to newly created buttons
        document.querySelectorAll('.qty-btn.minus').forEach(btn => {'''

new_btn_listeners = r'''        // Add event listeners to the variant selectors
        document.querySelectorAll('.cart-size-select').forEach(select => {
            select.addEventListener('change', (e) => {
                const idx = e.target.getAttribute('data-index');
                cart[idx].size = e.target.value;
                document.getElementById('checkout-form').classList.remove('submitted');
                updateCart();
            });
        });
        
        document.querySelectorAll('.cart-type-select').forEach(select => {
            select.addEventListener('change', (e) => {
                const idx = e.target.getAttribute('data-index');
                cart[idx].tShirtType = e.target.value;
                document.getElementById('checkout-form').classList.remove('submitted');
                updateCart();
            });
        });

        // Add event listeners to newly created buttons
        document.querySelectorAll('.qty-btn.minus').forEach(btn => {'''

if old_btn_listeners in js:
    js = js.replace(old_btn_listeners, new_btn_listeners)
else:
    print("Could not find button listeners block")

# 4. Enforce validation before submitting form
old_form_submit = r'''    checkoutForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        if (cart.length === 0) {
            showToast('Your cart is empty.');
            return;
        }'''
        
new_form_submit = r'''    checkoutForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        checkoutForm.classList.add('submitted'); // Add class to trigger red borders on missing selects
        
        if (cart.length === 0) {
            showToast('Your cart is empty.');
            return;
        }
        
        // Validate that all items have a size and type selected
        const unselectedItem = cart.find(item => !item.size || !item.tShirtType);
        if (unselectedItem) {
            showToast('Please select a Size and Type for all items in your cart.');
            reportError('Missing size/type at checkout', 'checkout');
            updateCart(); // Re-render to show red borders
            return;
        }'''

if old_form_submit in js:
    js = js.replace(old_form_submit, new_form_submit)
else:
    print("Could not find old form submit")

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Updated cart size logic")
