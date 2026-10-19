import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_logic = '''            // Build WhatsApp Message First
            let waMsg = `*NEW ORDER - CAMPUSMART*\\n---------------------\\n`;
            waMsg += `*Customer Details:*\\nName: ${name}\\nPhone: ${phone}\\n`;
            if (formData.get('alt_phone')) waMsg += `Alt Phone: ${formData.get('alt_phone')}\\n`;
            
            waMsg += `\\n*Delivery:*\\nOption: ${delivery}\\n`;
            if (address.replace(/,/g, '').trim()) waMsg += `Address: ${address}\\n`;
            
            waMsg += `\\n*Order Summary:*\\n`;'''

new_logic = '''            // Build WhatsApp Message First
            let waMsg = `*NEW ORDER - CAMPUSMART*\\n---------------------\\n`;
            waMsg += `*Customer Details:*\\nName: ${name}\\nPhone: ${phone}\\n`;
            if (formData.get('email')) waMsg += `Email: ${formData.get('email')}\\n`;
            
            waMsg += `\\n*Delivery:*\\nOption: ${delivery}\\n`;
            if (address.replace(/,/g, '').trim()) waMsg += `Address: ${address}\\n`;
            
            waMsg += `\\n*Order Summary:*\\n`;'''

js = js.replace(old_logic, new_logic)

old_logic2 = '''            const totalStr = document.getElementById('cart-total-price').textContent;
            waMsg += `\\n*Total Bill:* ${totalStr}\\n`;'''

new_logic2 = '''            const totalStr = document.getElementById('cart-total-price').textContent;
            if (formData.get('coupon_code')) {
                waMsg += `\\n*Coupon Applied:* ${formData.get('coupon_code')}\\n`;
            }
            waMsg += `\\n*Total Bill:* ${totalStr}\\n`;'''

js = js.replace(old_logic2, new_logic2)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Fixed missing email and coupon in WhatsApp payload")
