import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Let's replace the whole block from .promo-hero to .promo-early-bird inclusive
# Using regex to find the section
start_marker = r'/\* Promo Hero Section \*/'
end_marker = r'\.early-bird-price\s*\{[^\}]*\}'

match = re.search(f"{start_marker}.*?{end_marker}", css, re.DOTALL)
if match:
    old_css = match.group(0)
    print("Found old css block!")
else:
    print("Could not find old css block")

new_css = r'''/* Promo Hero Section */
.promo-hero {
    background-color: var(--bg-color);
    padding: 120px 1rem 4rem 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.promo-container {
    max-width: 600px; /* Compact width */
    width: 100%;
    
    /* Premium Black background */
    background: linear-gradient(135deg, #18181b 0%, #000000 100%);
    border-radius: 24px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    border: 1px solid rgba(255, 255, 255, 0.05);
    
    color: white;
    padding: 3rem 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 1.5rem;
    position: relative;
    overflow: hidden;
}

/* Orange Accent Line */
.promo-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(to right, #ea580c, #f97316); /* Orange accent */
}

.promo-info {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.promo-title {
    font-size: 3rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    color: #f97316; /* Orange text */
    text-transform: uppercase;
    letter-spacing: 2px;
}

.promo-pricing {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: rgba(255,255,255,0.05);
    padding: 0.75rem 1.5rem;
    border-radius: 12px;
}

.early-bird-price {
    font-size: 2.2rem;
    font-weight: 800;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.early-bird-price del {
    font-size: 1.2rem;
    color: rgba(255,255,255,0.5);
    font-weight: 500;
}

.limit-text {
    font-size: 0.9rem;
    color: rgba(255,255,255,0.7);
    margin-top: 0.25rem;
}

.promo-image-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 280px; /* Fixed height to prevent layout jumps during slideshow */
}

.hero-image {
    max-width: 100%;
    max-height: 260px;
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
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

.btn-shop-now {
    background: linear-gradient(to right, #ea580c, #f97316); /* Orange button */
    color: white;
    font-weight: 700;
    font-size: 1.1rem;
    padding: 1rem 3rem;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(234, 88, 12, 0.4);
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.btn-shop-now:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(234, 88, 12, 0.6);
    color: white;
}
'''
if match:
    css = css.replace(old_css, new_css)
    with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
        f.write(css)
    print("Replaced CSS")

