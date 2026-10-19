import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# We need to find the broken Delivery Details section and replace it.
# The broken section starts with <div class="checkout-section"> and ends right before <div class="checkout-section"> for Step 3.

broken_section_pattern = r'<div class="checkout-section">\s*<div class="checkout-section-header">\s*<span class="step-num">2</span>\s*<h5>Delivery Details</h5>.*?(?=<div class="checkout-section">\s*<div class="checkout-section-header">\s*<span class="step-num">3</span>)'

fixed_delivery_section = '''<div class="checkout-section">
                <div class="checkout-section-header">
                    <span class="step-num">2</span>
                    <h5>Delivery Details</h5>
                </div>
                
                <div class="form-row-2" style="margin-bottom: 1rem;">
                    <div class="form-group" style="flex: 1; margin-bottom: 0;">
                        <label class="floating-label-group">
                            <span class="label-text">Division *</span>
                            <select name="division" id="division" required>
                                <option value="">Select Division</option>
                            </select>
                        </label>
                    </div>
                    <div class="form-group" style="flex: 1; margin-bottom: 0;">
                        <label class="floating-label-group">
                            <span class="label-text">District *</span>
                            <select name="district" id="district" required disabled>
                                <option value="">Select District</option>
                            </select>
                        </label>
                    </div>
                </div>
                
                <div class="form-group" style="margin-bottom: 1rem;">
                    <label class="floating-label-group">
                        <span class="label-text">Upazila / Thana *</span>
                        <input type="text" name="upazila" placeholder="e.g. Mirpur" required>
                    </label>
                </div>
                
                <div class="form-group" style="margin-bottom: 1.5rem;">
                    <label class="floating-label-group">
                        <span class="label-text">Full Delivery Address *</span>
                        <textarea name="address" placeholder="Street, House/Apt No." required rows="2" style="padding-top:1.5rem;"></textarea>
                    </label>
                </div>

                <div class="form-group delivery-options-group"
                    style="background: var(--section-bg); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                    <p style="margin-bottom: 0.75rem; font-weight: 600; font-size: 0.95rem;">Delivery Method *</p>
                    <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                        <label
                            style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; font-size: 0.9rem;">
                            <input type="radio" name="delivery_option" value="Inside Campus" checked>
                            Inside Campus (Free)
                        </label>
                        <label
                            style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; font-size: 0.9rem;">
                            <input type="radio" name="delivery_option" value="Outside Campus">
                            Outside Campus
                        </label>
                    </div>
                    <p id="outside-campus-msg"
                        style="display: none; color: #4b5563; font-size: 0.85rem; margin-top: 0.75rem; font-weight: 500; background: rgba(0,0,0,0.05); padding: 0.5rem; border-radius: 4px; border-left: 3px solid #3b82f6;">
                        ℹ️ Subject to delivery partner. We'll call you and share the details promptly.</p>
                </div>
            </div>
            
            '''

new_html = re.sub(broken_section_pattern, fixed_delivery_section, html, flags=re.DOTALL)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(new_html)

print("Restored missing fields and fixed delivery section order.")
