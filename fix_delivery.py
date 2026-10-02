import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# 1. Update deliveryOptions event listener
old_delivery_options = r'''    deliveryOptions.forEach(option => {
        option.addEventListener('change', (e) => {
            if (e.target.value === 'Outside Campus') {
                outsideCampusMsg.style.display = 'block';
            } else {
                outsideCampusMsg.style.display = 'none';
            }
        });
    });'''
new_delivery_options = r'''    deliveryOptions.forEach(option => {
        option.addEventListener('change', (e) => {
            if (e.target.value === 'Outside Campus') {
                outsideCampusMsg.style.display = 'block';
            } else {
                outsideCampusMsg.style.display = 'none';
            }
            updateCart();
        });
    });'''
js = js.replace(old_delivery_options, new_delivery_options)

# 2. Add event listener to districtSelect
old_district_event = r'''        } else {
            districtSelect.disabled = true;
        }
    });'''
new_district_event = r'''        } else {
            districtSelect.disabled = true;
        }
    });
    
    districtSelect.addEventListener('change', () => {
        updateCart();
    });'''
if old_district_event in js:
    js = js.replace(old_district_event, new_district_event)
else:
    print("Could not find district event")

# 3. Modify updateCart function to calculate and display delivery charge
update_cart_target = r'''        cart.forEach((item, index) => {
            const effectivePrice = item.price - discountPerItem;
            total += effectivePrice * item.quantity;'''
            
update_cart_replacement = r'''        // Calculate Delivery Charge
        let deliveryCharge = 0;
        const isInsideCampus = document.querySelector('input[name="delivery_option"]:checked')?.value === 'Inside Campus';
        if (!isInsideCampus) {
            const district = document.getElementById('district').value;
            if (district === 'Dhaka' || district === 'Sylhet') {
                deliveryCharge = 80;
            } else if (district) {
                deliveryCharge = 130;
            } else {
                deliveryCharge = 130; // Default to 130 if not selected yet but outside campus
            }
        }
        
        let subtotal = 0;

        cart.forEach((item, index) => {
            const effectivePrice = item.price - discountPerItem;
            subtotal += effectivePrice * item.quantity;'''

if update_cart_target in js:
    js = js.replace(update_cart_target, update_cart_replacement)
else:
    print("Could not find cart loop target")

# Now update where total is set
total_set_target = r'''        cartTotalPrice.textContent = `৳ ${total}`;
        
        // Update Netlify Form hidden inputs
        orderDetailsInput.value = orderDetailsStr;
        totalAmountInput.value = total;
        
        // Update advance amount for customization
        const advanceAmountSpan = document.getElementById('advance-amount');
        if (advanceAmountSpan) {
            advanceAmountSpan.textContent = `৳ ${Math.ceil(total / 2)}`;
        }'''

total_set_replacement = r'''        const finalTotal = subtotal + deliveryCharge;
        
        const subtotalElement = document.getElementById('cart-subtotal-price');
        const deliveryChargeElement = document.getElementById('cart-delivery-price');
        
        if (subtotalElement) subtotalElement.textContent = `৳ ${subtotal}`;
        if (deliveryChargeElement) deliveryChargeElement.textContent = `৳ ${deliveryCharge}`;
        
        cartTotalPrice.textContent = `৳ ${finalTotal}`;
        
        // Add delivery info to order details
        if (deliveryCharge > 0) {
            orderDetailsStr += `\nDelivery Charge: ৳${deliveryCharge}`;
        } else {
            orderDetailsStr += `\nDelivery Charge: Free`;
        }
        
        // Update Netlify Form hidden inputs
        orderDetailsInput.value = orderDetailsStr;
        totalAmountInput.value = finalTotal;
        
        // Update advance amount for customization (50% of total including delivery)
        const advanceAmountSpan = document.getElementById('advance-amount');
        if (advanceAmountSpan) {
            advanceAmountSpan.textContent = `৳ ${Math.ceil(finalTotal / 2)}`;
        }'''

if total_set_target in js:
    js = js.replace(total_set_target, total_set_replacement)
else:
    print("Could not find total set target")
    
# Empty cart logic should also clear delivery charge fields
empty_cart_target = r'''            cartTotalPrice.textContent = '৳ 0';
            orderDetailsInput.value = '';'''
            
empty_cart_replacement = r'''            cartTotalPrice.textContent = '৳ 0';
            const subtotalElement = document.getElementById('cart-subtotal-price');
            const deliveryChargeElement = document.getElementById('cart-delivery-price');
            if (subtotalElement) subtotalElement.textContent = '৳ 0';
            if (deliveryChargeElement) deliveryChargeElement.textContent = '৳ 0';
            orderDetailsInput.value = '';'''

if empty_cart_target in js:
    js = js.replace(empty_cart_target, empty_cart_replacement)
else:
    print("Could not find empty cart target")


with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("JS updated successfully")
