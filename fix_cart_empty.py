import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

empty_cart_block = r'''        if \(cart.length === 0\) \{
            cartItemsContainer\.innerHTML = '<p style="text-align:center; color:#6b7280; margin-top:2rem;">Your cart is empty\.</p>';
            cartTotalPrice\.textContent = '৳ 0';
            orderDetailsInput\.value = '';
            totalAmountInput\.value = '0';
            return;
        \}'''

new_empty_cart_block = r'''        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<p style="text-align:center; color:#6b7280; margin-top:2rem; margin-bottom:2rem;">Your cart is empty.</p>';
            cartTotalPrice.textContent = '৳ 0';
            orderDetailsInput.value = '';
            totalAmountInput.value = '0';
            checkoutForm.style.display = 'none'; // Hide checkout form if cart is empty
            document.querySelector('.coupon-section').style.display = 'none';
            return;
        } else {
            checkoutForm.style.display = 'block';
            document.querySelector('.coupon-section').style.display = 'flex';
        }'''

js = re.sub(empty_cart_block, new_empty_cart_block, js)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Fixed empty cart checkout visibility")
