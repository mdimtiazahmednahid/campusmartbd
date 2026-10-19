import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# 1. Update radio buttons default state
old_inside = '<input type="radio" name="delivery_option" value="Inside Campus" checked>'
new_inside = '<input type="radio" name="delivery_option" value="Inside Campus" disabled>'
html = html.replace(old_inside, new_inside)

old_outside = '<input type="radio" name="delivery_option" value="Outside Campus">'
new_outside = '<input type="radio" name="delivery_option" value="Outside Campus" checked>'
html = html.replace(old_outside, new_outside)

# Add opacity and cursor styles for the disabled label directly in CSS later, or dynamically in JS.
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# 2. Add validation function and update listeners
js_addition = '''
    function checkCampusAvailability() {
        const divisionSelect = document.getElementById('division');
        const districtSelect = document.getElementById('district');
        const insideCampusRadio = document.querySelector('input[value="Inside Campus"]');
        const outsideCampusRadio = document.querySelector('input[value="Outside Campus"]');
        const insideCampusLabel = insideCampusRadio.closest('label');
        
        if (divisionSelect.value === 'Sylhet' && districtSelect.value === 'Sylhet') {
            insideCampusRadio.disabled = false;
            insideCampusLabel.style.opacity = '1';
            insideCampusLabel.style.pointerEvents = 'auto';
        } else {
            insideCampusRadio.disabled = true;
            insideCampusLabel.style.opacity = '0.5';
            insideCampusLabel.style.pointerEvents = 'none';
            
            if (insideCampusRadio.checked) {
                outsideCampusRadio.checked = true;
                document.getElementById('outside-campus-msg').style.display = 'block';
            }
        }
    }
'''

# Let's completely rewrite the division and district listeners to use this function instead of the messy old logic.
old_district_listener = '''    districtSelect.addEventListener('change', (e) => {
        const insideCampusRadio = document.querySelector('input[value="Inside Campus"]');
        const outsideCampusRadio = document.querySelector('input[value="Outside Campus"]');
        
        // If they pick a district other than Sylhet, they CANNOT be inside campus
        if (e.target.value !== 'Sylhet' && insideCampusRadio.checked) {
            outsideCampusRadio.checked = true;
            document.getElementById('outside-campus-msg').style.display = 'block';
        }
        updateCart();
    });'''

new_district_listener = '''    districtSelect.addEventListener('change', (e) => {
        checkCampusAvailability();
        updateCart();
    });'''

js = js.replace(old_district_listener, new_district_listener)

old_division_listener = '''        } else {
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

new_division_listener = '''        } else {
            districtSelect.disabled = true;
        }
        checkCampusAvailability();
        updateCart();
    });'''

js = js.replace(old_division_listener, new_division_listener)

# Remove the old "Force Sylhet" logic from the radio button click listener
old_radio_logic = '''        option.addEventListener('change', (e) => {
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
        });'''

new_radio_logic = '''        option.addEventListener('change', (e) => {
            if (e.target.value === 'Outside Campus') {
                outsideCampusMsg.style.display = 'block';
            } else {
                outsideCampusMsg.style.display = 'none';
            }
            updateCart();
        });'''

js = js.replace(old_radio_logic, new_radio_logic)

# Insert the function definition at the top of the DOMContentLoaded block
js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + js_addition)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Updated Campus Logic")
