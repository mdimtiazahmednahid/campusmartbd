import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

# Change overlay background to deep translucent red wine
old_overlay = "overlay.style.backgroundColor = 'rgba(15, 23, 42, 0.95)';"
new_overlay = "overlay.style.backgroundColor = 'rgba(42, 4, 13, 0.95)';" # Deep burgundy translucency
js = js.replace(old_overlay, new_overlay)

# Change price color from orange to vibrant ruby
old_price = "color:#f97316;"
new_price = "color:#ff4d66;" # Vibrant glowing ruby/pink so it pops on dark red
js = js.replace(old_price, new_price)

# Change Buy Now button to the 3-color premium red gradient
old_btn = "actionBtn.style.background = 'linear-gradient(135deg, #ea580c 0%, #f97316 100%)';"
new_btn = "actionBtn.style.background = 'linear-gradient(135deg, #6c0a1a 0%, #9b1122 45%, #42040d 100%)';"
js = js.replace(old_btn, new_btn)

old_shadow = "actionBtn.style.boxShadow = '0 8px 20px rgba(234, 88, 12, 0.4)';"
new_shadow = "actionBtn.style.boxShadow = '0 8px 24px rgba(108, 10, 26, 0.6)';"
js = js.replace(old_shadow, new_shadow)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Updated Lightbox to Red Wine theme")
