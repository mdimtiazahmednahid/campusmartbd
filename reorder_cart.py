import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# I will find the whole cart-sidebar block
pattern = r'(<div class="cart-sidebar" id="cart-sidebar">.*?<div class="cart-header">.*?</div>)(.*?)(<!-- Toast Notification -->)'
match = re.search(pattern, html, flags=re.DOTALL)

if not match:
    print("Failed to find cart sidebar block")
    exit(1)

prefix = match.group(1)
body = match.group(2)
suffix = match.group(3)

# Extract components from `body`
# 1. cart-items
cart_items_match = re.search(r'<div class="cart-items" id="cart-items">.*?</div>', body, flags=re.DOTALL)
cart_items = cart_items_match.group(0)

# 2. coupon section
coupon_match = re.search(r'<div class="coupon-section">.*?<div id="coupon-message" class="coupon-message"></div>', body, flags=re.DOTALL)
coupon_section = coupon_match.group(0)

# 3. totals
subtotal_match = re.search(r'<div class="cart-subtotal".*?</div>', body, flags=re.DOTALL)
delivery_match = re.search(r'<div class="cart-delivery-charge".*?</div>', body, flags=re.DOTALL)
total_match = re.search(r'<div class="cart-total".*?</div>', body, flags=re.DOTALL)
subtotal = subtotal_match.group(0)
delivery = delivery_match.group(0)
total = total_match.group(0)

# 4. Form inputs (Contact, Delivery, Customization)
# We find everything inside the form except the hidden inputs and submit button
form_start_match = re.search(r'<form name="checkout"[^>]*>', body, flags=re.DOTALL)
form_start = form_start_match.group(0)

bot_field_match = re.search(r'<!-- Netlify hidden input -->.*?</p>', body, flags=re.DOTALL)
bot_field = bot_field_match.group(0)

contact_match = re.search(r'<div class="checkout-section">.*?<h5>Contact Information</h5>.*?</div>\s*</div>', body, flags=re.DOTALL)
contact = contact_match.group(0)

delivery_details_match = re.search(r'<div class="checkout-section">.*?<h5>Delivery Details</h5>.*?</div>\s*</div>', body, flags=re.DOTALL)
delivery_details = delivery_details_match.group(0)

customization_match = re.search(r'<div class="checkout-section">.*?<h5>Customization</h5>.*?</div>\s*</div>', body, flags=re.DOTALL)
customization = customization_match.group(0)

hidden_inputs_match = re.search(r'<!-- Hidden inputs to store order data -->.*?</button>', body, flags=re.DOTALL)
hidden_inputs_and_button = hidden_inputs_match.group(0)

# Reassemble
new_sidebar = f'''{prefix}
    <form name="checkout" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="checkout-form" id="checkout-form" style="display: flex; flex-direction: column; flex: 1; overflow: hidden; margin: 0; padding: 0; height: calc(100vh - 70px);">
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

print("Successfully redesigned and reordered the cart!")
