import re

# Update index.html
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

old_html = r'''                <div class="promo-info">
                    <h1 class="promo-title">LAUNCH OFFER</h1>
                    <div class="promo-pricing">
                        <p class="early-bird-price">⚡ ৳499 <del>৳650</del></p>
                        <p class="limit-text">First 50 Orders • October Only</p>
                    </div>
                </div>
                
                <div class="promo-image-wrapper" id="hero-slideshow">
                    <img src="assets/kiloroad-black.png" alt="Premium Edition" class="hero-image active-slide" id="hero-image">
                </div>
                
                <a href="#collection" class="btn btn-shop-now">Shop Now</a>'''

new_html = r'''                <div class="promo-info">
                    <h1 class="promo-title">LAUNCH OFFER</h1>
                    <div class="promo-pricing">
                        <p class="early-bird-price">⚡ ৳499 <del>৳650</del></p>
                        <p class="limit-text">First 50 Orders</p>
                    </div>
                    <a href="#collection" class="btn btn-shop-now">Shop Now</a>
                </div>
                
                <div class="promo-image-wrapper" id="hero-slideshow">
                    <img src="assets/kiloroad-black.png" alt="Premium Edition" class="hero-image active-slide" id="hero-image">
                </div>'''

if old_html in html:
    html = html.replace(old_html, new_html)
    with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
        f.write(html)
    print("Updated HTML structure")
else:
    print("Could not find old HTML structure")

# Update style.css
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Replace the promo-container block and its children
start_marker = r'\.promo-hero\s*\{'
end_marker = r'\.btn-shop-now:hover\s*\{[^\}]*\}'

match = re.search(f"{start_marker}.*?{end_marker}", css, re.DOTALL)
if match:
    old_css = match.group(0)
else:
    print("Could not find old CSS block")
    exit()

new_css = r'''.promo-hero {
    background-color: var(--bg-color);
    padding: 100px 1rem 3rem 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.promo-container {
    max-width: 800px;
    width: 100%;
    
    /* Premium Navy Blue background */
    background: linear-gradient(135deg, #070f2b 0%, #1b1a55 100%);
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(37, 99, 235, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.05);
    
    color: white;
    padding: 2rem;
    display: flex;
    flex-direction: row; /* Horizontal layout */
    align-items: center;
    justify-content: space-between;
    text-align: left;
    gap: 1rem;
    position: relative;
    overflow: hidden;
}

/* Orange Accent Line */
.promo-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: linear-gradient(to bottom, #ea580c, #f97316); /* Orange accent on left */
}

.promo-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex: 1;
}

.promo-title {
    font-size: 2.2rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    color: #f97316; /* Orange text */
    text-transform: uppercase;
    letter-spacing: 1px;
}

.promo-pricing {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    background: rgba(255,255,255,0.05);
    padding: 0.5rem 1rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
}

.early-bird-price {
    font-size: 1.8rem;
    font-weight: 800;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.early-bird-price del {
    font-size: 1rem;
    color: rgba(255,255,255,0.5);
    font-weight: 500;
}

.limit-text {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.7);
    margin-top: 0.2rem;
}

.promo-image-wrapper {
    flex: 1;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    height: 180px;
}

.hero-image {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 15px 25px rgba(0,0,0,0.4));
    animation: float 6s ease-in-out infinite;
    transition: opacity 0.5s ease-in-out, transform 0.5s ease;
}

.hero-image.fade-out {
    opacity: 0;
    transform: scale(0.95);
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}

.btn-shop-now {
    background: linear-gradient(to right, #ea580c, #f97316); /* Orange button */
    color: white;
    font-weight: 700;
    font-size: 1rem;
    padding: 0.75rem 2rem;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(234, 88, 12, 0.4);
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
    display: inline-block;
}

.btn-shop-now:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(234, 88, 12, 0.6);
    color: white;
}'''

css = css.replace(old_css, new_css)

# Update mobile override if it exists, or just add one if it doesn't
mobile_override_old = r'''    .promo-hero {
        padding: 90px 1rem 2rem 1rem;
    }
    .promo-container {
        padding: 2rem 1.5rem;
    }
    .promo-title {
        font-size: 2.2rem;
    }
    .early-bird-price {
        font-size: 1.8rem;
    }'''

mobile_override_new = r'''    .promo-hero {
        padding: 80px 1rem 1rem 1rem;
    }
    .promo-container {
        padding: 1.5rem 1rem;
        flex-direction: row;
        align-items: center;
        gap: 0.5rem;
    }
    .promo-title {
        font-size: 1.5rem;
        letter-spacing: 0;
    }
    .early-bird-price {
        font-size: 1.3rem;
    }
    .promo-pricing {
        padding: 0.4rem 0.6rem;
        margin-bottom: 1rem;
    }
    .btn-shop-now {
        padding: 0.5rem 1rem;
        font-size: 0.85rem;
    }
    .promo-image-wrapper {
        height: 140px;
        flex: 0.8;
    }'''

if mobile_override_old in css:
    css = css.replace(mobile_override_old, mobile_override_new)
else:
    # If not found exactly, just append it into the max-width: 768px block
    mq_idx = css.find('@media (max-width: 768px) {')
    if mq_idx != -1:
        insert_idx = css.find('{', mq_idx) + 1
        css = css[:insert_idx] + '\n' + mobile_override_new + css[insert_idx:]

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Updated to horizontal rectangular layout")
