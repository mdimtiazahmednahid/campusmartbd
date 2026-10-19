import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# 1. Move WhatsApp URL generation ABOVE history save
old_submit_block = '''            // Save to Order History
            const orderInfo = {
                date: new Date().toLocaleString(),
                items: cart.map(item => `${item.title} (${item.quantity}x)`).join(', '),
                total: document.getElementById('cart-total-price').textContent
            };
            const history = JSON.parse(localStorage.getItem('campusMartHistory')) || [];
            history.push(orderInfo);
            localStorage.setItem('campusMartHistory', JSON.stringify(history));

            // Show toast
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);

            // Reset UI and state
            cart = [];
            isEarlyBirds = false;
            localStorage.removeItem('campusmart_coupon');
            if (couponInput) couponInput.value = '';
            // Build WhatsApp Message
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
            const whatsappUrl = `https://wa.me/8801600265376?text=${encodedWaMsg}`;'''

new_submit_block = '''            // Build WhatsApp Message First
            let waMsg = `*NEW ORDER - CAMPUSMART*\\n---------------------\\n`;
            waMsg += `*Customer Details:*\\nName: ${name}\\nPhone: ${phone}\\n`;
            if (formData.get('alt_phone')) waMsg += `Alt Phone: ${formData.get('alt_phone')}\\n`;
            
            waMsg += `\\n*Delivery:*\\nOption: ${delivery}\\n`;
            if (address.replace(/,/g, '').trim()) waMsg += `Address: ${address}\\n`;
            
            waMsg += `\\n*Order Summary:*\\n`;
            cart.forEach(item => {
                waMsg += `- ${item.title} (${item.tShirtType || 'N/A'}, Size: ${item.size || 'N/A'}) x${item.quantity}\\n`;
            });
            
            if (formData.get('is_customized') === 'on') {
                waMsg += `\\n*Customization:*\\nName: ${formData.get('custom_name')}\\nNumber: ${formData.get('custom_number')}\\n`;
                waMsg += `Advance: Paid\\n`;
                waMsg += `bKash/Nagad No: ${formData.get('sender_number')}\\nTrxID: ${formData.get('trx_id')}\\n`;
            }
            
            const totalStr = document.getElementById('cart-total-price').textContent;
            waMsg += `\\n*Total Bill:* ${totalStr}\\n`;
            
            const encodedWaMsg = encodeURIComponent(waMsg);
            const whatsappUrl = `https://wa.me/8801600265376?text=${encodedWaMsg}`;
            
            // Save to Order History with URL
            const orderInfo = {
                date: new Date().toLocaleString(),
                items: cart.map(item => `${item.title} (${item.quantity}x)`).join(', '),
                total: totalStr,
                waUrl: whatsappUrl
            };
            const history = JSON.parse(localStorage.getItem('campusMartHistory')) || [];
            history.push(orderInfo);
            localStorage.setItem('campusMartHistory', JSON.stringify(history));

            // Show toast
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);

            // Reset UI and state
            cart = [];
            isEarlyBirds = false;
            localStorage.removeItem('campusmart_coupon');
            if (couponInput) couponInput.value = '';'''

js = js.replace(old_submit_block, new_submit_block)

# 2. Add button to loadOrderHistory
old_history_render = '''        const item = document.createElement('div');
        item.className = 'history-item';
        item.innerHTML = `
            <div class="history-date">${order.date}</div>
            <div class="history-title">${order.items}</div>
            <div class="history-total">Total: ${order.total}</div>
        `;
        historyItems.appendChild(item);'''

new_history_render = '''        const item = document.createElement('div');
        item.className = 'history-item';
        item.style.position = 'relative';
        item.innerHTML = `
            <div class="history-date">${order.date}</div>
            <div class="history-title">${order.items}</div>
            <div class="history-total" style="margin-bottom: 0.5rem;">Total: ${order.total}</div>
            ${order.waUrl ? `<a href="${order.waUrl}" target="_blank" style="display:inline-flex; align-items:center; gap:0.25rem; font-size:0.75rem; background:#25D366; color:white; padding:0.3rem 0.6rem; border-radius:4px; font-weight:600; text-decoration:none;"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg> Forward to WhatsApp</a>` : ''}
        `;
        historyItems.appendChild(item);'''

js = js.replace(old_history_render, new_history_render)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Updated history forward logic")
