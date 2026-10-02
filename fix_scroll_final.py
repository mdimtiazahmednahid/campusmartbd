import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# 1. Fix Form scroll
# We need to give it display: flex; flex-direction: column; min-height: 0; flex: 1;
# Then inside the form, the content wrapper scrolls, and the footer stays sticky.
# Let's restore the perfect flexbox architecture.

# Find the form tag
form_pattern = r'<form name="checkout" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="checkout-form" id="checkout-form" style="[^"]+">'
form_replacement = '<form name="checkout" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="checkout-form" id="checkout-form" style="display: flex; flex-direction: column; flex: 1; min-height: 0; margin: 0; padding: 0;">'
html = re.sub(form_pattern, form_replacement, html)

# The content wrapper should have overflow-y: auto
# It currently has: class="cart-scrollable-content" style="padding: 1.5rem;"
scroll_wrapper = r'<div class="cart-scrollable-content" style="padding: 1.5rem;">'
scroll_replacement = '<div class="cart-scrollable-content" style="flex: 1; overflow-y: auto; padding: 1.5rem; -webkit-overflow-scrolling: touch;">'
html = html.replace(scroll_wrapper, scroll_replacement)

# 2. Fix Delivery Method box styling
old_delivery_box = r'style="background: var(--section-bg); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;"'
new_delivery_box = r'style="background: #f8fafc; padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color); margin-bottom: 1rem;"'
html = html.replace(old_delivery_box, new_delivery_box)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)
print("Applied final scroll fixes and styling")
