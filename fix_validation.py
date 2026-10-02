import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# 1. Update the delivery options change listener
delivery_toggle_pattern = r"deliveryOptions\.forEach\(option => \{.*?\}\);\n    \}\);"
# Wait, let's just do a regex replace on the entire block.
delivery_toggle_block = '''deliveryOptions.forEach(option => {
        option.addEventListener('change', (e) => {
            if (e.target.value === 'Outside Campus') {
                outsideCampusMsg.style.display = 'block';
            } else {
                outsideCampusMsg.style.display = 'none';
            }
            updateCart();
        });
    });'''

new_delivery_toggle_block = '''deliveryOptions.forEach(option => {
        option.addEventListener('change', (e) => {
            const divisionSelect = document.getElementById('division');
            const districtSelect = document.getElementById('district');
            
            if (e.target.value === 'Outside Campus') {
                outsideCampusMsg.style.display = 'block';
            } else {
                // User clicked Inside Campus. Force Sylhet!
                outsideCampusMsg.style.display = 'none';
                if (divisionSelect.value !== 'Sylhet') {
                    divisionSelect.value = 'Sylhet';
                    // Trigger change manually to populate districts
                    divisionSelect.dispatchEvent(new Event('change'));
                }
                districtSelect.value = 'Sylhet';
            }
            updateCart();
        });
    });'''

js = js.replace(delivery_toggle_block, new_delivery_toggle_block)

# 2. Update divisionSelect and districtSelect change listeners
# Currently:
#     districtSelect.addEventListener('change', () => {
#         updateCart();
#     });

old_district_listener = r"    districtSelect\.addEventListener\('change', \(\) => \{\n        updateCart\(\);\n    \}\);"
new_district_listener = '''    districtSelect.addEventListener('change', (e) => {
        const insideCampusRadio = document.querySelector('input[value="Inside Campus"]');
        const outsideCampusRadio = document.querySelector('input[value="Outside Campus"]');
        
        // If they pick a district other than Sylhet, they CANNOT be inside campus
        if (e.target.value !== 'Sylhet' && insideCampusRadio.checked) {
            outsideCampusRadio.checked = true;
            document.getElementById('outside-campus-msg').style.display = 'block';
        }
        updateCart();
    });'''

js = re.sub(old_district_listener, new_district_listener, js)

# We also need to add logic to divisionSelect
#     divisionSelect.addEventListener('change', (e) => { ...
#         if (selectedDiv && bdLocations[selectedDiv]) { ... }
#     });

old_division_listener = r"    divisionSelect\.addEventListener\('change', \(e\) => \{.*?\n        \}\n    \}\);"
# I will use re.sub with DOTALL to carefully replace it.
# Actually it's safer to just do a string replace for the end of the division listener
old_div_end = '''        } else {
            districtSelect.disabled = true;
        }
    });'''

new_div_end = '''        } else {
            districtSelect.disabled = true;
        }
        
        const insideCampusRadio = document.querySelector('input[value="Inside Campus"]');
        const outsideCampusRadio = document.querySelector('input[value="Outside Campus"]');
        if (selectedDiv !== 'Sylhet' && insideCampusRadio.checked) {
            outsideCampusRadio.checked = true;
            document.getElementById('outside-campus-msg').style.display = 'block';
        }
        updateCart();
    });'''

js = js.replace(old_div_end, new_div_end)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Updated JS validation")
