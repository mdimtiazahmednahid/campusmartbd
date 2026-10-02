import re
with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_str = r'''    checkoutForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        if (cart.length === 0) {
            showToast('Your cart is empty. Please add items before checking out.'); reportError('Attempted checkout with empty cart', 'checkout');
            return;
        }'''

new_str = r'''    checkoutForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        checkoutForm.classList.add('submitted'); // Add class to trigger red borders on missing selects
        
        if (cart.length === 0) {
            showToast('Your cart is empty. Please add items before checking out.'); reportError('Attempted checkout with empty cart', 'checkout');
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

js = js.replace(old_str, new_str)
with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Updated submit logic")
