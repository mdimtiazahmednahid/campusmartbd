import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_logic = '''    // Add to Cart Logic
    const handleAddToCart = (btn, openAfter = false) => {
        const id = btn.getAttribute('data-id');
        const title = btn.getAttribute('data-title');
        const price = parseInt(btn.getAttribute('data-price'));
        const image = btn.getAttribute('data-image');
        
        // Now, items are added directly to the cart without initial size/type.
        // If an identical item (same id, same empty size/type) exists, increment qty.
        const size = '';
        const tShirtType = '';'''

new_logic = '''    // Add to Cart Logic
    const handleAddToCart = (btn, openAfter = false) => {
        const id = btn.getAttribute('data-id');
        const title = btn.getAttribute('data-title');
        const price = parseInt(btn.getAttribute('data-price'));
        const image = btn.getAttribute('data-image');
        
        // Find the closest product card to read the selected size and type
        const card = btn.closest('.product-card');
        let size = '';
        let tShirtType = '';
        if (card) {
            const sizeSelect = card.querySelector('select[id^="size-"]');
            const typeSelect = card.querySelector('select[id^="type-"]');
            if (sizeSelect && sizeSelect.value) size = sizeSelect.value;
            if (typeSelect && typeSelect.value) tShirtType = typeSelect.value;
        }'''

js = js.replace(old_logic, new_logic)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Fixed handleAddToCart to read dropdowns")
