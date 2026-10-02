import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Pattern to replace: from <div id="customization-details" down to <div class="checkout-section order-summary-section" style="margin-top: 2rem;">
pattern = r'<div id="customization-details".*?(?=<div class="checkout-section order-summary-section" style="margin-top: 2rem;">)'

fixed_block = '''<div id="customization-details"
                            style="display: none; margin-top: 1rem; padding-top: 1rem; border-top: 1px dashed rgba(16, 185, 129, 0.3);">
                            
                            <div class="form-row-2">
                                <div class="form-group" style="flex: 2; margin-bottom: 1rem;">
                                    <label class="floating-label-group">
                                        <span class="label-text">Customized Name *</span>
                                        <input type="text" name="custom_name" placeholder="e.g. CAMPUSMART">
                                    </label>
                                </div>
                                <div class="form-group" style="flex: 1; margin-bottom: 1rem;">
                                    <label class="floating-label-group">
                                        <span class="label-text">Number *</span>
                                        <input type="text" name="custom_number" placeholder="e.g. 10">
                                    </label>
                                </div>
                            </div>

                            <div
                                style="background: white; padding: 1rem; border-radius: 6px; margin-bottom: 1rem; text-align: center; border: 1px solid var(--border-color);">
                                <p style="font-size: 0.95rem; margin-bottom: 0.5rem; font-weight: 700;">50% Advance Required: <span
                                        id="advance-amount" style="color: #dc2626;">৳ 0</span></p>
                                <p style="font-size: 0.85rem; color: var(--text-light); margin-bottom: 0.5rem;">Pay via bKash/Nagad:</p>
                                <button type="button" id="copy-number-btn"
                                    style="background: #f8fafc; border: 1px dashed var(--border-color); padding: 0.5rem 1rem; border-radius: 4px; font-weight: 700; cursor: pointer; font-family: inherit; font-size: 1.1rem; width: 100%; display: flex; justify-content: center; align-items: center; gap: 0.5rem; color: var(--text-color);">
                                    +880 1600-265376
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                        stroke-width="2">
                                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                    </svg>
                                </button>
                                <p id="copy-toast"
                                    style="display: none; color: var(--primary-color); font-size: 0.8rem; margin-top: 0.5rem;">
                                    Number copied!</p>
                            </div>

                            <div class="form-row-2">
                                <div class="form-group" style="flex: 1; margin-bottom: 1rem;">
                                    <label class="floating-label-group">
                                        <span class="label-text">Your bKash/Nagad Number *</span>
                                        <input type="tel" name="sender_number" placeholder="01XXXXXXXXX">
                                    </label>
                                </div>
                                <div class="form-group" style="flex: 1; margin-bottom: 1rem;">
                                    <label class="floating-label-group">
                                        <span class="label-text">Transaction ID *</span>
                                        <input type="text" name="trx_id" placeholder="Transaction ID">
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            
            '''

new_html = re.sub(pattern, fixed_block, html, flags=re.DOTALL)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(new_html)
print("Restored missing customization fields and closed tags")
