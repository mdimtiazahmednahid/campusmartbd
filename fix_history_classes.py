import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_open = '''function openHistory() {
    loadOrderHistory();
    historySidebar.classList.add('open');
    historyOverlay.classList.add('open');
}

function closeHistoryFn() {
    historySidebar.classList.remove('open');
    historyOverlay.classList.remove('open');
}'''

new_open = '''function openHistory() {
    loadOrderHistory();
    historySidebar.classList.add('active');
    historyOverlay.classList.add('active');
}

function closeHistoryFn() {
    historySidebar.classList.remove('active');
    historyOverlay.classList.remove('active');
}'''

js = js.replace(old_open, new_open)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Fixed CSS classes for history sidebar")
