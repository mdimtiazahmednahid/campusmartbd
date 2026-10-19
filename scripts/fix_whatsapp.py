import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_block = '''            updateCart();
            // We intentionally don't clear the form inputs so the address stays for next time
            closeCart();
        })'''

new_block = '''            // Build WhatsApp Message
            let waMsg = `*NEW ORDER - CAMPUSMART*\\n---------------------\\n`;
            waMsg += `*Customer Details:*\\nName: ${name}\\nPhone: ${phone}\\n`;
            if (formData.get('alt_phone')) waMsg += `Alt Phone: ${formData.get('alt_phone')}\\n`;
            
            waMsg += `\\n*Delivery:*\\nOption: ${delivery}\\n`;
            if (address.replace(/,/g, '').trim()) waMsg += `Address: ${address}\\n`;
            
            waMsg += `\\n*Order Summary:*\\n`;
            let tempCart = JSON.parse(localStorage.getItem('campusmart_cart')) || []; // use saved cart since we just cleared it above
            tempCart.forEach(item => {
                waMsg += `- ${item.title} (${item.tShirtType || 'N/A'}, Size: ${item.size || 'N/A'}) x${item.quantity}\\n`;
            });
            
            if (formData.get('is_customized') === 'on') {
                waMsg += `\\n*Customization:*\\nName: ${formData.get('custom_name')}\\nNumber: ${formData.get('custom_number')}\\n`;
                waMsg += `Advance: Paid\\n`;
                waMsg += `bKash/Nagad No: ${formData.get('sender_number')}\\nTrxID: ${formData.get('trx_id')}\\n`;
            }
            
            waMsg += `\\n*Total Bill:* ${orderInfo.total}\\n`;
            
            const encodedWaMsg = encodeURIComponent(waMsg);
            const whatsappUrl = `https://wa.me/8801600265376?text=${encodedWaMsg}`;
            
            updateCart();
            // We intentionally don't clear the form inputs so the address stays for next time
            closeCart();
            
            // Redirect to WhatsApp after short delay to let PDF download trigger
            setTimeout(() => {
                window.location.href = whatsappUrl;
            }, 1000);
        })'''

js = js.replace(old_block, new_block)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Added WhatsApp redirection")
