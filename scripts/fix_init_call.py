import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_init = '''    // Initial render
    updateCart();
});'''

new_init = '''    // Initial render
    checkCampusAvailability();
    updateCart();
});'''

js = js.replace(old_init, new_init)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Added init call")
