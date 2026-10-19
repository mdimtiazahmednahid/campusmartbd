import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_logic = '''        if (divisionSelect.value === 'Sylhet' && districtSelect.value === 'Sylhet') {
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
        }'''

new_logic = '''        if (divisionSelect.value === 'Sylhet' && districtSelect.value === 'Sylhet') {
            insideCampusRadio.disabled = false;
            insideCampusLabel.style.display = 'flex';
        } else {
            insideCampusRadio.disabled = true;
            insideCampusLabel.style.display = 'none';
            
            if (insideCampusRadio.checked) {
                outsideCampusRadio.checked = true;
                document.getElementById('outside-campus-msg').style.display = 'block';
            }
        }'''

js = js.replace(old_logic, new_logic)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Updated Inside Campus visibility")
