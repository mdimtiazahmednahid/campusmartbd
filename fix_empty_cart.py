import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_empty = '''        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<p style="text-align:center; color:#6b7280; margin-top:2rem; margin-bottom:2rem;">Your cart is empty.</p>';'''

new_empty = '''        if (cart.length === 0) {
            cartItemsContainer.innerHTML = `
                <div style="text-align:center; padding: 3rem 1rem; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
                    <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5" style="margin-bottom: 1.5rem;">
                        <circle cx="9" cy="21" r="1"></circle>
                        <circle cx="20" cy="21" r="1"></circle>
                        <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                    </svg>
                    <h4 style="font-size: 1.3rem; color: #1e293b; margin-bottom: 0.5rem; font-weight: 700;">Your Cart is Empty</h4>
                    <p style="color: #64748b; margin-bottom: 2rem; font-size: 0.95rem;">Looks like you haven't added any jerseys yet.</p>
                    <button onclick="document.getElementById('close-cart').click()" style="background: #3b82f6; color: white; border: none; padding: 0.8rem 1.8rem; border-radius: 12px; font-weight: 600; cursor: pointer; transition: transform 0.1s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(59,130,246,0.3);" onmousedown="this.style.transform='scale(0.96)'" onmouseup="this.style.transform='scale(1)'" onmouseleave="this.style.transform='scale(1)'">Browse Collection</button>
                </div>
            `;'''

js = js.replace(old_empty, new_empty)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Added gorgeous empty state to cart")
