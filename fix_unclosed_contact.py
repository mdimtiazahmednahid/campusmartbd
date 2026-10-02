import re
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# I will find the transition from Contact Information to Delivery Details.
# It currently looks like:
#                             </label>
#                         </div>
#                     </div>
#                 
#             <div class="checkout-section">
#                 <div class="checkout-section-header">
#                     <span class="step-num">2</span>
#                     <h5>Delivery Details</h5>

pattern = r'(<span class="label-text">Email Address \*</span>.*?</div>\s*</div>\s*)(<div class="checkout-section">\s*<div class="checkout-section-header">\s*<span class="step-num">2</span>\s*<h5>Delivery Details</h5>)'

match = re.search(pattern, html, flags=re.DOTALL)
if match:
    new_html = html[:match.start()] + match.group(1) + '</div>\n            ' + match.group(2) + html[match.end():]
    with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
        f.write(new_html)
    print("Fixed missing div in contact section")
else:
    print("Could not find the pattern")
