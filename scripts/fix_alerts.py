import re

# 1. Add to index.html
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Add toaster and hidden form right before </body>
toaster_html = r'''    <!-- Toaster Container -->
    <div id="toast-container" class="toast-container"></div>
    
    <!-- Hidden Error Report Form for Netlify -->
    <form name="error-report" netlify netlify-honeypot="bot-field" hidden>
        <input type="text" name="error_message">
        <input type="text" name="user_action">
    </form>
</body>'''

html = html.replace('</body>', toaster_html)
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)

# 2. Add CSS
css_str = r'''
/* Toast Notifications */
.toast-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.toast {
    background-color: #ef4444; /* red-500 for error */
    color: white;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 600;
    font-size: 0.95rem;
    transform: translateX(120%);
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.toast.toast-success {
    background-color: #10b981; /* emerald-500 */
}
.toast.show {
    transform: translateX(0);
    opacity: 1;
}
'''
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'a') as f:
    f.write(css_str)

# 3. Add JS functions and replace alerts
with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

toast_functions = r'''// Toast Notification System
function showToast(message, type = 'error') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    const icon = type === 'error' ? '⚠️' : '✅';
    toast.innerHTML = `<span style="font-size: 1.2rem;">${icon}</span> <span>${message}</span>`;
    
    container.appendChild(toast);
    
    setTimeout(() => toast.classList.add('show'), 10);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Error Reporting to Netlify Forms
function reportError(message, actionContext) {
    const formData = new URLSearchParams();
    formData.append('form-name', 'error-report');
    formData.append('error_message', message);
    formData.append('user_action', actionContext);
    
    fetch('/', {
        method: 'POST',
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData.toString()
    }).catch(err => console.error('Error reporting failed', err));
}

'''
js = toast_functions + js

js = js.replace("alert('Please select a Size and T-shirt Type before adding to cart.');", 
                "showToast('Please select a Size and T-shirt Type before adding to cart.'); reportError('Missing size/type selection', 'add_to_cart');")

js = js.replace("alert('Your cart is empty. Please add items before checking out.');", 
                "showToast('Your cart is empty. Please add items before checking out.'); reportError('Attempted checkout with empty cart', 'checkout');")

js = js.replace("alert('There was an issue submitting your order. Please try again.');", 
                "showToast('There was an issue submitting your order. Please try again.'); reportError('Order submission failed', 'form_submit');")

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Added Toaster and Error Reporting")
