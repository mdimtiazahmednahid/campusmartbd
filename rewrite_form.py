import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Extract from <form name="checkout"...> to </form>
pattern = r'(<form name="checkout"[^>]*>)(.*?)(</form>)'
match = re.search(pattern, html, flags=re.DOTALL)

if match:
    form_start = match.group(1)
    
    new_form_content = r'''
                <!-- Netlify hidden input -->
                <input type="hidden" name="form-name" value="checkout">
                <p style="display: none;">
                    <label>Don't fill this out if you're human: <input name="bot-field" /></label>
                </p>
                <!-- Hidden inputs to store order data -->
                <input type="hidden" name="order_details" id="order_details">
                <input type="hidden" name="total_amount" id="total_amount">
                <input type="hidden" name="coupon_code" id="hidden_coupon_code">

                <div class="checkout-section">
                    <div class="checkout-section-header">
                        <span class="step-num">1</span>
                        <h5>Contact Information</h5>
                    </div>
                    <div class="form-group">
                        <input type="text" name="name" placeholder="Full Name" required>
                    </div>
                    <div class="form-row-2">
                        <div class="form-group" style="flex:1;">
                            <input type="tel" name="phone" placeholder="Phone Number" required>
                        </div>
                        <div class="form-group" style="flex:1;">
                            <input type="email" name="email" placeholder="Email Address" required>
                        </div>
                    </div>
                </div>

                <div class="checkout-section">
                    <div class="checkout-section-header">
                        <span class="step-num">2</span>
                        <h5>Delivery Details</h5>
                    </div>
                    
                    <div class="form-group delivery-options-group"
                        style="background: var(--section-bg); padding: 1rem; border-radius: 8px;">
                        <p style="margin-bottom: 0.75rem; font-weight: 600; font-size: 0.95rem;">Delivery Method</p>
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

                    <div class="form-row-2" style="margin-bottom: 1rem;">
                        <div class="form-group" style="flex: 1; margin-bottom: 0;">
                            <select name="division" id="division" required
                                style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 8px; outline: none; font-family: inherit;">
                                <option value="">Select Division</option>
                            </select>
                        </div>
                        <div class="form-group" style="flex: 1; margin-bottom: 0;">
                            <select name="district" id="district" required disabled
                                style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 8px; outline: none; font-family: inherit;">
                                <option value="">Select District</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <input type="text" name="upazila" placeholder="Upazila / Thana" required>
                    </div>
                    <div class="form-group">
                        <textarea name="address" placeholder="Full Delivery Address (Street, House/Apt No.)" required
                            rows="2"></textarea>
                    </div>
                </div>

                <div class="checkout-section">
                    <div class="checkout-section-header">
                        <span class="step-num">3</span>
                        <h5>Customization</h5>
                    </div>
                    
                    <div class="form-group customization-group"
                        style="background: rgba(16, 185, 129, 0.05); padding: 1rem; border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.2);">
                        <label
                            style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; font-weight: 600; color: var(--primary-color);">
                            <input type="checkbox" id="is_customized" name="is_customized"
                                style="width: auto; margin: 0; cursor: pointer; accent-color: var(--primary-color);">
                            Yes, customize my jersey (Name & Number)
                        </label>

                        <div id="customization-details"
                            style="display: none; margin-top: 1rem; padding-top: 1rem; border-top: 1px dashed rgba(16, 185, 129, 0.3);">
                            
                            <div class="form-row-2">
                                <div class="form-group" style="flex: 2; margin-bottom: 1rem;">
                                    <input type="text" name="custom_name" placeholder="Customized name">
                                </div>
                                <div class="form-group" style="flex: 1; margin-bottom: 1rem;">
                                    <input type="text" name="custom_number" placeholder="Number">
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
                                    <input type="tel" name="sender_number" placeholder="Your sending number">
                                </div>
                                <div class="form-group" style="flex: 1; margin-bottom: 1rem;">
                                    <input type="text" name="trx_id" placeholder="Transaction ID">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <button type="submit" class="btn btn-primary btn-checkout" style="margin-top: 1rem;">Confirm Order & Pay</button>
'''
    
    html = html.replace(match.group(2), new_form_content)
    
    with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
        f.write(html)
    print("Form replaced successfully.")

# Also add CSS for checkout structure
css_str = r'''
/* Checkout Form Structure */
.checkout-section {
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--border-color);
}
.checkout-section:last-of-type {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}
.checkout-section-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1.25rem;
}
.checkout-section-header .step-num {
    background: var(--text-color);
    color: white;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    font-size: 0.8rem;
    font-weight: 700;
}
.checkout-section-header h5 {
    font-size: 1.1rem;
    font-weight: 600;
    margin: 0;
    color: var(--text-color);
}
.form-row-2 {
    display: flex;
    gap: 1rem;
}
@media (max-width: 480px) {
    .form-row-2 {
        flex-direction: column;
        gap: 0;
    }
}
'''
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'a') as f:
    f.write(css_str)

