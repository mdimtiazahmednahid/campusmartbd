with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

old_total = r'''            <div class="cart-total">
                <span>Total:</span>
                <span id="cart-total-price">৳ 0</span>
            </div>'''

new_totals = r'''            <div class="cart-subtotal" style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 0.95rem; color: var(--text-light); font-weight: 500;">
                <span>Subtotal:</span>
                <span id="cart-subtotal-price">৳ 0</span>
            </div>
            <div class="cart-delivery-charge" style="display: flex; justify-content: space-between; margin-bottom: 1rem; font-size: 0.95rem; color: var(--text-light); font-weight: 500;">
                <span>Delivery Charge:</span>
                <span id="cart-delivery-price">৳ 0</span>
            </div>
            <div class="cart-total" style="border-top: 1px dashed var(--border-color); padding-top: 1rem;">
                <span>Total:</span>
                <span id="cart-total-price">৳ 0</span>
            </div>'''

if old_total in html:
    html = html.replace(old_total, new_totals)
    with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
        f.write(html)
    print("HTML replaced")
else:
    print("Could not find HTML block")
