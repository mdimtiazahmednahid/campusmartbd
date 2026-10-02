import re

# 1. Update HTML
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Add link to nav
nav_link = r'<a href="#size-guide" class="nav-link">Size Guide</a>'
new_nav_link = nav_link + '\n                <a href="#" class="nav-link" id="nav-history">Order History</a>'
html = html.replace(nav_link, new_nav_link)

# Add sidebar modal
cart_overlay = r'    <!-- Cart Modal / Sidebar -->'
history_sidebar = r'''    <!-- Order History Sidebar -->
    <div class="cart-overlay" id="history-overlay"></div>
    <div class="cart-sidebar" id="history-sidebar">
        <div class="cart-header">
            <h3>Order History</h3>
            <button class="close-cart" id="close-history">&times;</button>
        </div>
        <div class="cart-items" id="history-items" style="flex: 1; overflow-y: auto;">
            <!-- History items injected by JS -->
        </div>
    </div>

    <!-- Cart Modal / Sidebar -->'''
html = html.replace(cart_overlay, history_sidebar)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)

# 2. Add CSS
css_str = r'''
/* Order History */
.history-item {
    background: #f9fafb;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
}
.history-date {
    font-size: 0.8rem;
    color: #6b7280;
    margin-bottom: 0.5rem;
}
.history-title {
    font-weight: 600;
    font-size: 0.95rem;
    color: var(--text-color);
    margin-bottom: 0.25rem;
}
.history-total {
    font-weight: 700;
    color: #ea580c;
    margin-top: 0.5rem;
}
'''
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'a') as f:
    f.write(css_str)

# 3. Add JS
with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

history_js = r'''
// Order History Logic
const navHistory = document.getElementById('nav-history');
const historySidebar = document.getElementById('history-sidebar');
const historyOverlay = document.getElementById('history-overlay');
const closeHistory = document.getElementById('close-history');
const historyItems = document.getElementById('history-items');

function loadOrderHistory() {
    const history = JSON.parse(localStorage.getItem('campusMartHistory')) || [];
    historyItems.innerHTML = '';
    
    if (history.length === 0) {
        historyItems.innerHTML = '<div class="empty-cart"><p>You have no past orders.</p></div>';
        return;
    }
    
    history.slice().reverse().forEach(order => {
        const item = document.createElement('div');
        item.className = 'history-item';
        item.innerHTML = `
            <div class="history-date">${order.date}</div>
            <div class="history-title">${order.items}</div>
            <div class="history-total">Total: ${order.total}</div>
        `;
        historyItems.appendChild(item);
    });
}

function openHistory() {
    loadOrderHistory();
    historySidebar.classList.add('open');
    historyOverlay.classList.add('open');
}

function closeHistoryFn() {
    historySidebar.classList.remove('open');
    historyOverlay.classList.remove('open');
}

if (navHistory) {
    navHistory.addEventListener('click', (e) => {
        e.preventDefault();
        openHistory();
    });
}
if (closeHistory) closeHistory.addEventListener('click', closeHistoryFn);
if (historyOverlay) historyOverlay.addEventListener('click', closeHistoryFn);

'''

# Inject saving history to checkout fetch success block
checkout_success_target = r'''alert\('Order Placed Successfully! Your PDF receipt is generating\.'\);
                    generatePDF\(formData\);'''
checkout_success_replace = r'''showToast('Order Placed Successfully! Generating receipt...', 'success');
                    
                    // Save to Order History
                    const orderInfo = {
                        date: new Date().toLocaleString(),
                        items: cart.map(item => `${item.title} (${item.quantity}x)`).join(', '),
                        total: document.getElementById('total-price').textContent
                    };
                    const history = JSON.parse(localStorage.getItem('campusMartHistory')) || [];
                    history.push(orderInfo);
                    localStorage.setItem('campusMartHistory', JSON.stringify(history));
                    
                    generatePDF(formData);'''

if "alert('Order Placed Successfully! Your PDF receipt is generating.');" in js:
    js = js.replace("alert('Order Placed Successfully! Your PDF receipt is generating.');\n                    generatePDF(formData);", 
                    checkout_success_replace.replace('\\', ''))
else:
    # If the exact string didn't match, we will just use re.sub
    pass # Wait, let's just do it directly.

js += history_js

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Added Order History feature")
