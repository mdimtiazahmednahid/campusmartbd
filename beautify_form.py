import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# I will replace the raw inputs with labeled inputs.
# Step 1: Contact Information
html = html.replace('<div class="form-group">\n                        <input type="text" name="name" placeholder="Full Name *" required>\n                    </div>',
'''<div class="form-group">
                        <label class="floating-label-group">
                            <span class="label-text">Full Name *</span>
                            <input type="text" name="name" placeholder="e.g. John Doe" required>
                        </label>
                    </div>''')

html = html.replace('<div class="form-group" style="flex:1;">\n                            <input type="tel" name="phone" placeholder="Phone Number *" required>\n                        </div>',
'''<div class="form-group" style="flex:1;">
                            <label class="floating-label-group">
                                <span class="label-text">Phone Number *</span>
                                <input type="tel" name="phone" placeholder="e.g. 017XXXXXXXX" required>
                            </label>
                        </div>''')

html = html.replace('<div class="form-group" style="flex:1;">\n                            <input type="email" name="email" placeholder="Email Address *" required>\n                        </div>',
'''<div class="form-group" style="flex:1;">
                            <label class="floating-label-group">
                                <span class="label-text">Email Address *</span>
                                <input type="email" name="email" placeholder="e.g. name@example.com" required>
                            </label>
                        </div>''')

# Step 2: Delivery
html = html.replace('<div class="form-group" style="flex: 1; margin-bottom: 0;">\n                            <select name="division" id="division" required\n                                style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 8px; outline: none; font-family: inherit;">\n                                <option value="">Select Division *</option>\n                            </select>\n                        </div>',
'''<div class="form-group" style="flex: 1; margin-bottom: 0;">
                            <label class="floating-label-group">
                                <span class="label-text">Division *</span>
                                <select name="division" id="division" required>
                                    <option value="">Select Division</option>
                                </select>
                            </label>
                        </div>''')

html = html.replace('<div class="form-group" style="flex: 1; margin-bottom: 0;">\n                            <select name="district" id="district" required disabled\n                                style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 8px; outline: none; font-family: inherit;">\n                                <option value="">Select District *</option>\n                            </select>\n                        </div>',
'''<div class="form-group" style="flex: 1; margin-bottom: 0;">
                            <label class="floating-label-group">
                                <span class="label-text">District *</span>
                                <select name="district" id="district" required disabled>
                                    <option value="">Select District</option>
                                </select>
                            </label>
                        </div>''')

html = html.replace('<div class="form-group">\n                        <input type="text" name="upazila" placeholder="Upazila / Thana *" required>\n                    </div>',
'''<div class="form-group">
                        <label class="floating-label-group">
                            <span class="label-text">Upazila / Thana *</span>
                            <input type="text" name="upazila" placeholder="e.g. Mirpur" required>
                        </label>
                    </div>''')

html = html.replace('<div class="form-group">\n                        <textarea name="address" placeholder="Full Delivery Address (Street, House/Apt No.) *" required\n                            rows="2"></textarea>\n                    </div>',
'''<div class="form-group">
                        <label class="floating-label-group">
                            <span class="label-text">Full Delivery Address *</span>
                            <textarea name="address" placeholder="Street, House/Apt No." required rows="2" style="padding-top:1.5rem;"></textarea>
                        </label>
                    </div>''')

# Step 3: Customization
html = html.replace('<div class="form-group" style="flex: 2; margin-bottom: 1rem;">\n                                    <input type="text" name="custom_name" placeholder="Customized name *">\n                                </div>',
'''<div class="form-group" style="flex: 2; margin-bottom: 1rem;">
                                    <label class="floating-label-group">
                                        <span class="label-text">Customized Name *</span>
                                        <input type="text" name="custom_name" placeholder="e.g. CAMPUSMART">
                                    </label>
                                </div>''')

html = html.replace('<div class="form-group" style="flex: 1; margin-bottom: 1rem;">\n                                    <input type="text" name="custom_number" placeholder="Number *">\n                                </div>',
'''<div class="form-group" style="flex: 1; margin-bottom: 1rem;">
                                    <label class="floating-label-group">
                                        <span class="label-text">Number *</span>
                                        <input type="text" name="custom_number" placeholder="e.g. 10">
                                    </label>
                                </div>''')

html = html.replace('<div class="form-group" style="flex: 1; margin-bottom: 1rem;">\n                                    <input type="tel" name="sender_number" placeholder="Your sending number *">\n                                </div>',
'''<div class="form-group" style="flex: 1; margin-bottom: 1rem;">
                                    <label class="floating-label-group">
                                        <span class="label-text">Your bKash/Nagad Number *</span>
                                        <input type="tel" name="sender_number" placeholder="01XXXXXXXXX">
                                    </label>
                                </div>''')

html = html.replace('<div class="form-group" style="flex: 1; margin-bottom: 1rem;">\n                                    <input type="text" name="trx_id" placeholder="Trx number (Optional)">\n                                </div>',
'''<div class="form-group" style="flex: 1; margin-bottom: 1rem;">
                                    <label class="floating-label-group">
                                        <span class="label-text">TrxID (Optional)</span>
                                        <input type="text" name="trx_id" placeholder="Transaction ID">
                                    </label>
                                </div>''')

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)
print("Updated HTML")
