import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_func = '''function loadOrderHistory() {
    const history = JSON.parse(localStorage.getItem('campusMartHistory')) || [];
    historyItems.innerHTML = '';'''

new_func = '''function loadOrderHistory() {
    let history = [];
    try {
        const stored = localStorage.getItem('campusMartHistory');
        if (stored && stored !== 'undefined' && stored !== 'null') {
            history = JSON.parse(stored);
        }
    } catch (e) {
        console.error('Failed to parse history', e);
        history = [];
    }
    
    if (!Array.isArray(history)) {
        history = [];
    }
    
    historyItems.innerHTML = '';'''

js = js.replace(old_func, new_func)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Added try-catch to order history parser")
