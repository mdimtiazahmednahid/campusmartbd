import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# I will completely rewrite the cart-sidebar from scratch to ensure it is pristine and not duplicated.
# Let's extract the exact components from the current html (taking only the FIRST occurrence of each).

cart_items = re.search(r'<div class="cart-items" id="cart-items">.*?</div>', html, flags=re.DOTALL).group(0)
coupon_section = re.search(r'<div class="coupon-section">.*?<div id="coupon-message" class="coupon-message"></div>', html, flags=re.DOTALL).group(0)
subtotal = re.search(r'<div class="cart-subtotal".*?</div>', html, flags=re.DOTALL).group(0)
delivery = re.search(r'<div class="cart-delivery-charge".*?</div>', html, flags=re.DOTALL).group(0)
total = re.search(r'<div class="cart-total".*?</div>', html, flags=re.DOTALL).group(0)

# For the form sections, I must strictly match just ONE block of them.
contact = re.search(r'<div class="checkout-section">\s*<div class="checkout-section-header">\s*<span class="step-num">1</span>\s*<h5>Contact Information</h5>.*?</div>\s*</div>', html, flags=re.DOTALL).group(0)
delivery_details = re.search(r'<div class="checkout-section">\s*<div class="checkout-section-header">\s*<span class="step-num">2</span>\s*<h5>Delivery Details</h5>.*?</div>\s*</div>', html, flags=re.DOTALL).group(0)
customization = re.search(r'<div class="checkout-section">\s*<div class="checkout-section-header">\s*<span class="step-num">3</span>\s*<h5>Customization</h5>.*?</div>\s*</div>', html, flags=re.DOTALL).group(0)

hidden_inputs_and_button = re.search(r'<!-- Hidden inputs to store order data -->.*?</button>', html, flags=re.DOTALL).group(0)
bot_field = re.search(r'<!-- Netlify hidden input -->.*?</p>', html, flags=re.DOTALL).group(0)


pattern = r'(<div class="cart-sidebar" id="cart-sidebar">.*?<div class="cart-header">.*?</div>)(.*?)(<!-- Toast Notification -->)'
match = re.search(pattern, html, flags=re.DOTALL)
prefix = match.group(1)
suffix = match.group(3)

new_sidebar = f'''{prefix}
    <form name="checkout" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="checkout-form" id="checkout-form" style="display: flex; flex-direction: column; flex: 1; overflow: hidden; margin: 0; padding: 0; min-height: 0;">
        <div class="cart-scrollable-content" style="flex: 1; overflow-y: auto; padding: 1.5rem;">
            {bot_field}
            
            {contact}
            
            {delivery_details}
            
            {customization}
            
            <div class="checkout-section order-summary-section" style="margin-top: 2rem;">
                <div class="checkout-section-header">
                    <span class="step-num">4</span>
                    <h5>Order Summary</h5>
                </div>
                
                {cart_items}
                
                <div style="background: #f8fafc; padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); margin-top: 1rem;">
                    {coupon_section}
                    
                    <div style="margin-top: 1rem;">
                        {subtotal}
                        {delivery}
                        {total}
                    </div>
                </div>
            </div>
        </div>
        
        <div class="cart-footer-sticky" style="padding: 1.5rem; background: white; border-top: 1px solid var(--border-color); flex-shrink: 0; box-shadow: 0 -4px 10px rgba(0,0,0,0.02);">
            {hidden_inputs_and_button}
        </div>
    </form>
    </div>
'''

new_html = html[:match.start()] + new_sidebar + suffix + html[match.end():]

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(new_html)
print("Removed duplications!")
