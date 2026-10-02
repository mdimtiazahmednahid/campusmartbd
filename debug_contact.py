import re
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

contact = re.search(r'<div class="checkout-section">\s*<div class="checkout-section-header">\s*<span class="step-num">1</span>\s*<h5>Contact Information</h5>', html, flags=re.DOTALL)
print("Start of contact:", contact.start())
