with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Replacements for required fields in Checkout Form
replacements = {
    'placeholder="Full Name"': 'placeholder="Full Name *"',
    'placeholder="Phone Number"': 'placeholder="Phone Number *"',
    'placeholder="Email Address"': 'placeholder="Email Address *"',
    '<option value="">Select Division</option>': '<option value="">Select Division *</option>',
    '<option value="">Select District</option>': '<option value="">Select District *</option>',
    'placeholder="Upazila / Thana"': 'placeholder="Upazila / Thana *"',
    'placeholder="Full Delivery Address (Street, House/Apt No.)"': 'placeholder="Full Delivery Address (Street, House/Apt No.) *"',
    
    # Customization fields (conditionally required)
    'placeholder="Customized name"': 'placeholder="Customized name *"',
    'placeholder="Number"': 'placeholder="Number *"',
    'placeholder="Your sending number"': 'placeholder="Your sending number *"',
    
    # Contact form
    'placeholder="Your Name"': 'placeholder="Your Name *"',
    'placeholder="Your Email"': 'placeholder="Your Email *"',
    'placeholder="Your Message"': 'placeholder="Your Message *"'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)
print("Added asterisks to mandatory fields")
