import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Replace <span class="delivery-card-subtitle">Calculated</span>
old_subtitle = '<span class="delivery-card-subtitle">Calculated</span>'
new_subtitle = '<span class="delivery-card-subtitle" id="dynamic-outside-charge">৳80 - ৳130</span>'

html = html.replace(old_subtitle, new_subtitle)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# In script.js, updateCart() handles deliveryCharge logic.
# Let's insert the dynamic label update right where we calculate deliveryCharge.

old_logic = '''        let deliveryCharge = 0;
        const isInsideCampus = document.querySelector('input[name="delivery_option"]:checked')?.value === 'Inside Campus';
        if (!isInsideCampus) {
            const district = document.getElementById('district').value;
            if (district === 'Dhaka' || district === 'Sylhet') {
                deliveryCharge = 80;
            } else if (district) {
                deliveryCharge = 130;
            } else {
                deliveryCharge = 130; // Default to 130 if not selected yet but outside campus
            }
        }'''

new_logic = '''        let deliveryCharge = 0;
        const isInsideCampus = document.querySelector('input[name="delivery_option"]:checked')?.value === 'Inside Campus';
        const district = document.getElementById('district').value;
        
        let outsideChargeText = "৳80 - ৳130";
        if (district === 'Dhaka' || district === 'Sylhet') {
            outsideChargeText = "৳80";
        } else if (district) {
            outsideChargeText = "৳130";
        }
        
        const dynamicChargeEl = document.getElementById('dynamic-outside-charge');
        if (dynamicChargeEl) {
            dynamicChargeEl.textContent = outsideChargeText;
        }

        if (!isInsideCampus) {
            if (district === 'Dhaka' || district === 'Sylhet') {
                deliveryCharge = 80;
            } else if (district) {
                deliveryCharge = 130;
            } else {
                deliveryCharge = 130; // Default to 130 if not selected yet but outside campus
            }
        }'''

js = js.replace(old_logic, new_logic)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Updated dynamic charge display")
