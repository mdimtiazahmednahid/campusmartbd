import re
with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

js = js.replace('<option value="">Select District</option>', '<option value="">Select District *</option>')

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Updated JS district dropdown text")
