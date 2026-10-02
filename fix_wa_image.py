import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_logic = '''            waMsg += `\\n*Order Summary:*\\n`;
            cart.forEach(item => {
                waMsg += `- ${item.title} (${item.tShirtType || 'N/A'}, Size: ${item.size || 'N/A'}) x${item.quantity}\\n`;
            });
            
            if (formData.get('is_customized') === 'on') {
                waMsg += `\\n*Customization:*\\nName: ${formData.get('custom_name')}\\nNumber: ${formData.get('custom_number')}\\n`;
                waMsg += `Advance: Paid\\n`;
                waMsg += `bKash/Nagad No: ${formData.get('sender_number')}\\nTrxID: ${formData.get('trx_id')}\\n`;
            }
            
            const totalStr = document.getElementById('cart-total-price').textContent;
            waMsg += `\\n*Total Bill:* ${totalStr}\\n`;'''

new_logic = '''            waMsg += `\\n*Order Summary:*\\n`;
            let imageUrls = [];
            cart.forEach(item => {
                waMsg += `- ${item.title} (${item.tShirtType || 'N/A'}, Size: ${item.size || 'N/A'}) x${item.quantity}\\n`;
                if (item.image) {
                    try {
                        imageUrls.push(new URL(item.image, window.location.href).href);
                    } catch(e){}
                }
            });
            
            if (formData.get('is_customized') === 'on') {
                waMsg += `\\n*Customization:*\\nName: ${formData.get('custom_name')}\\nNumber: ${formData.get('custom_number')}\\n`;
                waMsg += `Advance: Paid\\n`;
                waMsg += `bKash/Nagad No: ${formData.get('sender_number')}\\nTrxID: ${formData.get('trx_id')}\\n`;
            }
            
            const totalStr = document.getElementById('cart-total-price').textContent;
            waMsg += `\\n*Total Bill:* ${totalStr}\\n`;
            
            // Append product image link so WhatsApp automatically generates an image preview thumbnail
            if (imageUrls.length > 0) {
                waMsg += `\\n*Product Image Reference:*\\n${imageUrls[0]}\\n`;
            }'''

js = js.replace(old_logic, new_logic)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Added image URL to WA message")
