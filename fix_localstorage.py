import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_logic = r'''        const savedVal = localStorage.getItem(`campusmart_user_${input.name}`);
        if (savedVal) {
            input.value = savedVal;
        }'''

new_logic = r'''        const savedVal = localStorage.getItem(`campusmart_user_${input.name}`);
        if (savedVal && savedVal !== 'undefined' && savedVal !== 'null') {
            input.value = savedVal;
        } else {
            input.value = '';
        }'''

js = js.replace(old_logic, new_logic)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)

print("Fixed localstorage loading")
