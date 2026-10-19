import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_logic = '''        document.querySelectorAll('.cart-size-select').forEach(select => {
            select.addEventListener('change', (e) => {
                const idx = e.target.getAttribute('data-index');
                cart[idx].size = e.target.value;
                document.getElementById('checkout-form').classList.remove('submitted');
                updateCart();
            });
        });'''

new_logic = '''        document.querySelectorAll('.cart-size-select').forEach(select => {
            select.addEventListener('change', (e) => {
                const idx = e.target.getAttribute('data-index');
                const oldSize = cart[idx].size;
                const newSize = e.target.value;
                
                const wasPlus = (oldSize === 'XXL' || oldSize === '3XL');
                const isPlus = (newSize === 'XXL' || newSize === '3XL');
                
                if (!wasPlus && isPlus) {
                    cart[idx].price += 50;
                } else if (wasPlus && !isPlus) {
                    cart[idx].price -= 50;
                }
                
                cart[idx].size = newSize;
                document.getElementById('checkout-form').classList.remove('submitted');
                updateCart();
            });
        });'''

js = js.replace(old_logic, new_logic)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Fixed cart size dropdown to update prices correctly")
