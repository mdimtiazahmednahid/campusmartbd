import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Replace the entire block
old_block = '''/* =========================================
   OVERRIDE: PREMIUM NAVY PRODUCT CARDS
   ========================================= */

.product-card {
    background: #0f172a !important; /* Premium Navy Blue */
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2) !important;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    padding: 1rem !important;
}

.product-card:hover {
    border-color: rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.1) !important; /* Removed the orange outline, using sleek dark shadow */
    transform: translateY(-6px) !important;
}

.product-image-container {
    background: #ffffff !important; /* Pure White Image Background */
    border-radius: 16px !important;
    position: relative;
    padding: 1rem !important;
    aspect-ratio: 1 / 1 !important; /* Fixed the height to be perfectly square and short */
    margin-bottom: 1.5rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.product-image-container img {
    max-width: 100% !important;
    max-height: 100% !important;
    object-fit: contain !important;
}

.product-title {
    color: #f8fafc !important; /* White text on Navy */
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
}

.product-price {
    color: #f97316 !important; /* Orange price text */
    font-weight: 800 !important;
}

.original-price {
    color: #64748b !important;
}

.btn-add-cart {
    background: rgba(255, 255, 255, 0.05) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    transition: all 0.2s ease !important;
}

.btn-add-cart:hover {
    background: #f97316 !important;
    color: #ffffff !important;
    border-color: transparent !important;
}

.btn-buy-now {
    background: linear-gradient(135deg, #ea580c 0%, #f97316 100%) !important; /* Orange gradient button */
    color: #ffffff !important;
    border: none !important;
    box-shadow: 0 8px 20px rgba(234, 88, 12, 0.3) !important;
}

.btn-buy-now:hover {
    box-shadow: 0 12px 24px rgba(234, 88, 12, 0.4) !important;
    transform: translateY(-2px) !important;
}'''

new_block = '''/* =========================================
   OVERRIDE: PREMIUM RED WINE PRODUCT CARDS
   ========================================= */

.product-card {
    background: #ffffff !important;
    border-radius: 20px !important;
    border: 1px solid rgba(155, 17, 34, 0.08) !important;
    box-shadow: 0 8px 24px rgba(108, 10, 26, 0.03) !important;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    padding: 1rem !important;
}

.product-card:hover {
    border-color: rgba(155, 17, 34, 0.3) !important;
    box-shadow: 0 20px 40px rgba(108, 10, 26, 0.12), 0 0 0 1px rgba(155, 17, 34, 0.1) !important;
    transform: translateY(-6px) !important;
}

.product-image-container {
    background: #ffffff !important; /* Pure White as requested */
    border-radius: 16px !important;
    position: relative;
    padding: 1rem !important;
    aspect-ratio: 1 / 1 !important; /* Fixed height! */
    margin-bottom: 1.5rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: 1px solid rgba(0,0,0,0.03) !important;
}

.product-image-container img {
    max-width: 100% !important;
    max-height: 100% !important;
    object-fit: contain !important;
}

.product-title {
    color: #42040d !important; /* Deep Burgundy */
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
}

.product-price {
    color: #9b1122 !important; /* Vibrant Ruby */
    font-weight: 800 !important;
}

.original-price {
    color: #a3b1c6 !important;
}

.btn-add-cart {
    background: linear-gradient(135deg, #fff5f6 0%, #fef1f2 100%) !important;
    color: #9b1122 !important;
    border: 1px solid rgba(155, 17, 34, 0.2) !important;
    transition: all 0.2s ease !important;
}

.btn-add-cart:hover {
    background: linear-gradient(135deg, #9b1122 0%, #6c0a1a 100%) !important;
    color: #ffffff !important;
    border-color: transparent !important;
    box-shadow: 0 8px 16px rgba(155, 17, 34, 0.2) !important;
    transform: translateY(-2px) !important;
}

.btn-buy-now {
    background: linear-gradient(135deg, #6c0a1a 0%, #9b1122 45%, #42040d 100%) !important; /* Match Launch Offer */
    color: #ffffff !important;
    box-shadow: 0 8px 20px rgba(108, 10, 26, 0.2) !important;
    border: none !important;
}

.btn-buy-now:hover {
    box-shadow: 0 12px 24px rgba(108, 10, 26, 0.3) !important;
    transform: translateY(-2px) !important;
}'''

if old_block in css:
    css = css.replace(old_block, new_block)
    with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
        f.write(css)
    print("Reverted to Red Wine Product Cards")
else:
    print("Old block not found!")
