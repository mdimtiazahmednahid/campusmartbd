import re

# Update index.html
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

old_hero = r'''        <section id="home" class="promo-hero">
            <div class="container promo-container">
                <div class="promo-content">
                    <p class="promo-subtitle" style="font-size: 1.2rem; font-weight: 600; letter-spacing: 2px; color: rgba(255,255,255,0.8); margin-bottom: 0.5rem;">CAMPUS MART</p>
                    <h1 class="promo-title">LAUNCH OFFER</h1>
                    
                    <div class="promo-pricing">
                        <p class="sale-price">৳550 <del style="font-size: 1.2rem; color: rgba(255,255,255,0.6); font-weight: 500; margin-left: 0.5rem;">৳650</del></p>
                    </div>
                    
                    <div class="promo-early-bird">
                        <p class="early-bird-price">⚡ ৳499</p>
                        <p class="limit-text">First 50 Orders • October Only</p>
                    </div>
                    
                    <a href="#collection" class="btn btn-white">Shop Now</a>
                </div>
                <div class="promo-image-wrapper">
                    <img src="assets/kiloroad-white.png" alt="Featured Edition Polo" class="hero-image" id="hero-image">
                </div>
            </div>
        </section>'''

new_hero = r'''        <section id="home" class="promo-hero">
            <div class="promo-container">
                <div class="promo-info">
                    <h1 class="promo-title">LAUNCH OFFER</h1>
                    <div class="promo-pricing">
                        <p class="early-bird-price">⚡ ৳499 <del>৳650</del></p>
                        <p class="limit-text">First 50 Orders • October Only</p>
                    </div>
                </div>
                
                <div class="promo-image-wrapper">
                    <img src="assets/kiloroad-white.png" alt="Featured Edition Polo" class="hero-image" id="hero-image">
                </div>
                
                <a href="#collection" class="btn btn-shop-now">Shop Now</a>
            </div>
        </section>'''

html = html.replace(old_hero, new_hero)

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)


# Update style.css
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Replace the promo-hero css
old_hero_css = r'''/* Promo Hero Section */
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
}

.promo-content {
    flex: 1;
    max-width: 500px;
}

.promo-image-wrapper {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

.hero-image {
    max-width: 90%;
    height: auto;
    filter: drop-shadow(0 20px 30px rgba(0,0,0,0.3));
    animation: float 6s ease-in-out infinite;
    transition: opacity 0.5s ease-in-out;
}

.hero-image.fade-out {
    opacity: 0;
}

@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-15px) rotate(2deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

.promo-subtitle {
    text-transform: uppercase;
}

.promo-title {
    font-size: 4rem;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 1rem;
    color: white;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.promo-pricing {
    margin-bottom: 0.5rem;
}

.sale-price {
    font-size: 3.5rem;
    font-weight: 800;
    color: #facc15;
    line-height: 1;
}

.promo-early-bird {
    background: rgba(255,255,255,0.1);
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    display: inline-block;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255,255,255,0.2);
}

.early-bird-price {
    font-size: 2.5rem;
    font-weight: 800;
    color: #10b981;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.limit-text {
    font-size: 0.9rem;
    color: rgba(255,255,255,0.9);
    margin-top: 0.25rem;
}'''

new_hero_css = r'''/* Promo Hero Section */
.promo-hero {
    background-color: var(--bg-color);
    padding: 100px 1rem 2rem 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.promo-container {
    max-width: 600px; /* Small, compact promo board */
    width: 100%;
    
    /* Matching logo orange color */
    background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(234, 88, 12, 0.25);
    
    color: white;
    padding: 2rem 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 1.5rem;
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
    background: rgba(255,255,255,0.3);
}

.promo-info {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.promo-image-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.hero-image {
    max-width: 250px; /* Much smaller image */
    height: auto;
    filter: drop-shadow(0 15px 25px rgba(0,0,0,0.3));
    animation: float 6s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-10px) rotate(2deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

.promo-title {
    font-size: 2.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    color: white;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.promo-pricing {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: rgba(0,0,0,0.15);
    padding: 0.75rem 1.5rem;
    border-radius: 12px;
}

.early-bird-price {
    font-size: 2rem;
    font-weight: 800;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.early-bird-price del {
    font-size: 1.2rem;
    color: rgba(255,255,255,0.7);
    font-weight: 500;
}

.limit-text {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.9);
    margin-top: 0.25rem;
}

.btn-shop-now {
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

css = css.replace(old_hero_css, new_hero_css)

# Remove the mobile overrides for promo hero since it's already mobile-first/column layout now
old_mobile = r'''    .promo-hero {
        padding: 90px 1rem 2rem 1rem;
    }

    .promo-container {
        padding: 2rem 1.5rem;
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }

    .promo-title {
        font-size: 2.2rem;
    }

    .sale-price {
        font-size: 2.5rem;
    }

    .early-bird-price {
        font-size: 3rem;
    }'''

new_mobile = r'''    .promo-hero {
        padding: 85px 1rem 1.5rem 1rem;
    }
'''

css = css.replace(old_mobile, new_mobile)

# Also fix btn-white which was removed in index.html if it exists somewhere else? It's fine, we added btn-shop-now

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Updated styling and HTML")
