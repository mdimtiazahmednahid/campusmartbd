import re

# Update index.html
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Add an ID to the image wrapper and the image for the slideshow
old_hero = r'''                <div class="promo-image-wrapper">
                    <img src="assets/kiloroad-white.png" alt="Featured Edition Polo" class="hero-image" id="hero-image">
                </div>'''

new_hero = r'''                <div class="promo-image-wrapper" id="hero-slideshow">
                    <img src="assets/kiloroad-black.png" alt="Premium Edition" class="hero-image active-slide" id="hero-image">
                </div>'''

html = html.replace(old_hero, new_hero)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)

# Update style.css
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

old_css = r'''    /* Matching logo orange color */
    background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(234, 88, 12, 0.25);'''

new_css = r'''    /* Premium Black background */
    background: linear-gradient(135deg, #111111 0%, #000000 100%);
    border-radius: 20px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    border: 1px solid rgba(255, 255, 255, 0.05);'''
css = css.replace(old_css, new_css)

old_accent = r'''/* Subtle accent line on the promo board */
.promo-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: rgba(255,255,255,0.3);
}'''

new_accent = r'''/* Subtle accent line on the promo board */
.promo-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(to right, #ea580c, #f97316); /* Orange accent */
}'''
css = css.replace(old_accent, new_accent)

old_title = r'''.promo-title {
    font-size: 2.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    color: white;
    text-transform: uppercase;
    letter-spacing: 1px;
}'''

new_title = r'''.promo-title {
    font-size: 2.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    color: #f97316; /* Orange text */
    text-transform: uppercase;
    letter-spacing: 1px;
}'''
css = css.replace(old_title, new_title)

old_price = r'''.early-bird-price {
    font-size: 2rem;
    font-weight: 800;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}'''

new_price = r'''.early-bird-price {
    font-size: 2rem;
    font-weight: 800;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}'''
css = css.replace(old_price, new_price)

old_btn = r'''.btn-shop-now {
    background-color: white;
    color: #ea580c;
    font-weight: 700;
    font-size: 1.1rem;
    padding: 0.75rem 2rem;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    width: 80%;
    max-width: 300px;
}

.btn-shop-now:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    color: #c2410c;
}'''

new_btn = r'''.btn-shop-now {
    background: linear-gradient(to right, #ea580c, #f97316); /* Orange button */
    color: white;
    font-weight: 700;
    font-size: 1.1rem;
    padding: 0.75rem 2rem;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(234, 88, 12, 0.4);
    transition: all 0.3s ease;
    width: 80%;
    max-width: 300px;
}

.btn-shop-now:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(234, 88, 12, 0.6);
    color: white;
}'''
css = css.replace(old_btn, new_btn)

# Ensure no fade animation is conflicting
old_fade = r'''.hero-image {
    max-width: 250px; /* Much smaller image */
    height: auto;
    filter: drop-shadow(0 15px 25px rgba(0,0,0,0.3));
    animation: float 6s ease-in-out infinite;
}'''

new_fade = r'''.hero-image {
    max-width: 250px; 
    height: auto;
    filter: drop-shadow(0 15px 25px rgba(0,0,0,0.3));
    animation: float 6s ease-in-out infinite;
    transition: opacity 0.5s ease-in-out;
}
.hero-image.fade-out {
    opacity: 0;
}'''
css = css.replace(old_fade, new_fade)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

# Update script.js to add slideshow logic
with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

slideshow_code = r'''
    // Hero Slideshow
    const heroImage = document.getElementById('hero-image');
    if (heroImage) {
        const slideImages = [
            'assets/kiloroad-black.png',
            'assets/kiloroad-navy.png',
            'assets/kiloroad-white.png',
            'assets/sustverse-white.png',
            'assets/sustverse-red.png',
            'assets/sustverse-grey.png'
        ];
        let currentSlide = 0;
        
        setInterval(() => {
            heroImage.classList.add('fade-out');
            setTimeout(() => {
                currentSlide = (currentSlide + 1) % slideImages.length;
                heroImage.src = slideImages[currentSlide];
                heroImage.classList.remove('fade-out');
            }, 500); // Wait for fade out to complete
        }, 3000); // Change image every 3 seconds
    }
'''

# Find a good place to insert this in script.js (e.g. before "Smooth scrolling")
if "Hero Slideshow" not in js:
    js = js.replace('// Smooth scrolling', slideshow_code + '\n    // Smooth scrolling')
    with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
        f.write(js)

print("Updated premium styling and slideshow script")
