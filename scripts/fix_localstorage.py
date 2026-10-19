import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_persist = '''        // Load existing data if available
        const savedVal = localStorage.getItem(`campusmart_user_${input.name}`);
        if (savedVal && savedVal !== 'undefined' && savedVal !== 'null') {
            input.value = savedVal;
        } else {
            input.value = '';
        }

        // Save on input/change
        input.addEventListener('change', (e) => {
            localStorage.setItem(`campusmart_user_${e.target.name}`, e.target.value);
        });'''

new_persist = '''        // Load existing data if available
        const savedVal = localStorage.getItem(`campusmart_user_${input.name}`);
        if (savedVal && savedVal !== 'undefined' && savedVal !== 'null') {
            if (input.type === 'radio') {
                if (input.value === savedVal) {
                    input.checked = true;
                }
            } else if (input.type === 'checkbox') {
                input.checked = savedVal === 'true';
            } else {
                input.value = savedVal;
            }
        } else if (input.type !== 'radio' && input.type !== 'checkbox') {
            input.value = '';
        }

        // Save on input/change
        input.addEventListener('change', (e) => {
            if (e.target.type === 'checkbox') {
                localStorage.setItem(`campusmart_user_${e.target.name}`, e.target.checked);
            } else {
                localStorage.setItem(`campusmart_user_${e.target.name}`, e.target.value);
            }
        });'''

js = js.replace(old_persist, new_persist)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Fixed LocalStorage overwriting radio values")
