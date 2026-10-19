import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Replace the promo-hero and promo-container CSS
old_css = r'''/* Promo Hero Section */
.promo-hero {
    background: radial-gradient(circle at right center, #dc2626, #991b1b, #450a0a);
    color: white;
    padding: 90px 1rem 3rem 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.promo-container {
    max-width: 1000px;
    width: 100%;
    color: white;
    padding: 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
    text-align: left;
}'''

new_css = r'''/* Promo Hero Section */
.promo-hero {
    background-color: var(--bg-color); /* White background instead of red */
    padding: 110px 1rem 3rem 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.promo-container {
    max-width: 1000px;
    width: 100%;
    
    /* Make it a rounded promo board */
    background: linear-gradient(135deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.6) 100%), url('https://images.unsplash.com/photo-1558769132-cb1fac0840c2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80') center/cover;
    background-color: #222;
    border-radius: 24px;
    box-shadow: 0 20px 40px rgba(220, 38, 38, 0.15);
    
    color: white;
    padding: 3rem 4rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
    text-align: left;
    position: relative;
    overflow: hidden;
}

/* Subtle accent line on the promo board */
.promo-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(to right, #ef4444, #dc2626, #991b1b);
}'''

css = css.replace(old_css, new_css)

# Also fix mobile padding for promo-hero and promo-container
old_mobile_css = r'''    .promo-hero {
        padding: 90px 1rem 2rem 1rem;
    }

    .promo-container {
        padding: 0;
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }'''

new_mobile_css = r'''    .promo-hero {
        padding: 90px 1rem 2rem 1rem;
    }

    .promo-container {
        padding: 2rem 1.5rem;
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }'''

css = css.replace(old_mobile_css, new_mobile_css)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Updated promo CSS")
