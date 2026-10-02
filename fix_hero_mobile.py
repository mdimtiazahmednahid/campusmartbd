import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Fix mobile order
old_promo_container = '''    .promo-container {
        padding: 2rem 1.5rem;
        flex-direction: column;
        align-items: center;'''

new_promo_container = '''    .promo-container {
        padding: 2rem 1.5rem;
        flex-direction: column-reverse; /* Image on top, button on bottom */
        align-items: center;'''

css = css.replace(old_promo_container, new_promo_container)

# Fix dancing image by ensuring object-fit and fixed sizing
old_hero_image = '''.hero-image {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 15px 25px rgba(0,0,0,0.4));
    animation: float 6s ease-in-out infinite;
    transition: opacity 0.5s ease-in-out, transform 0.5s ease;
}'''

new_hero_image = '''.hero-image {
    width: 100%;
    height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 15px 25px rgba(0,0,0,0.4));
    animation: float 6s ease-in-out infinite;
    transition: opacity 0.5s ease-in-out, transform 0.5s ease;
}'''

css = css.replace(old_hero_image, new_hero_image)

# Ensure mobile wrapper has a steady aspect ratio so it doesn't jump
old_promo_mobile = '''    .promo-image-wrapper {
        height: 200px;
        width: 100%;
        display: flex;
        justify-content: center;
    }'''

new_promo_mobile = '''    .promo-image-wrapper {
        height: 260px; /* Slightly taller for better view */
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }'''

css = css.replace(old_promo_mobile, new_promo_mobile)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)
print("Fixed hero mobile layout and image dancing")
