import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# The block to remove
hidden_inputs = r'''                <!-- Hidden inputs to store order data -->
                <input type="hidden" name="order_details" id="order_details">
                <input type="hidden" name="total_amount" id="total_amount">
                <input type="hidden" name="coupon_code" id="hidden_coupon_code">'''

# Remove it from the top
if hidden_inputs in html:
    html = html.replace(hidden_inputs, '')
    
    # Add it to the bottom, right before the submit button
    submit_btn = r'<button type="submit" class="btn btn-primary btn-checkout"'
    
    html = html.replace(submit_btn, hidden_inputs + '\n\n                <button type="submit" class="btn btn-primary btn-checkout"')
    
    with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
        f.write(html)
    print("Moved hidden inputs to the bottom of the form")
else:
    print("Could not find hidden inputs block")
