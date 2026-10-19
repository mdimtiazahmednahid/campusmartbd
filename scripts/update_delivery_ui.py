import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Pattern to replace
pattern = r'<div class="form-group delivery-options-group".*?</p>\s*</div>'

# Ensure we use re.DOTALL
new_html_block = '''<div class="form-group delivery-options-group">
                    <p>Delivery Method *</p>
                    <div class="delivery-cards-wrapper">
                        <label class="delivery-card-label">
                            <input type="radio" name="delivery_option" value="Inside Campus" checked>
                            <span class="delivery-card-title">Inside Campus</span>
                            <span class="delivery-card-subtitle">Free</span>
                        </label>
                        <label class="delivery-card-label">
                            <input type="radio" name="delivery_option" value="Outside Campus">
                            <span class="delivery-card-title">Outside Campus</span>
                            <span class="delivery-card-subtitle">Calculated</span>
                        </label>
                    </div>
                    <p id="outside-campus-msg"
                        style="display: none; color: #4b5563; font-size: 0.85rem; margin-top: 0.75rem; font-weight: 500; background: rgba(0,0,0,0.05); padding: 0.5rem; border-radius: 4px; border-left: 3px solid #ff8c00;">
                        ℹ️ Subject to delivery partner. We'll call you to confirm.</p>
                </div>'''

# Execute replace
replaced_html = re.sub(pattern, new_html_block, html, flags=re.DOTALL)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(replaced_html)
print("Updated delivery UI")
