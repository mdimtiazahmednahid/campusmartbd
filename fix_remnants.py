import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'r') as f:
    css = f.read()

# Remove stray leftover classes that we no longer need (if they exist outside the replaced block)
leftovers = [
    r'\.promo-content\s*\{[^\}]*\}',
    r'\.promo-subtitle\s*\{[^\}]*\}',
    r'\.sale-price\s*\{[^\}]*\}',
    r'\.btn-shop-now\s*\{[^\}]*\}' # wait, I just added btn-shop-now in the new block! Don't remove it.
]

for l in leftovers[:3]:
    css = re.sub(l, '', css)

# Also fix the mobile media queries that might override our new styles
mobile_override = r'''    \.promo-hero\s*\{[^\}]*\}
\s*\.promo-container\s*\{[^\}]*\}
\s*\.promo-title\s*\{[^\}]*\}
\s*\.sale-price\s*\{[^\}]*\}
\s*\.early-bird-price\s*\{[^\}]*\}'''

match = re.search(mobile_override, css)
if match:
    print("Found mobile overrides!")
    css = css.replace(match.group(0), r'''    .promo-hero {
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
    }''')
else:
    # Less strict search
    print("Trying less strict mobile override search")
    mobile2 = r'''    \.promo-hero \{
        padding: 90px 1rem 2rem 1rem;
    \}

    \.promo-container \{
        padding: 0;
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    \}

    \.promo-title \{
        font-size: 2\.2rem;
    \}

    \.sale-price \{
        font-size: 2\.5rem;
    \}

    \.early-bird-price \{
        font-size: 3rem;
    \}'''
    
    if re.search(mobile2, css):
        print("Found strict mobile override")
        css = re.sub(mobile2, r'''    .promo-hero {
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
    }''', css)

with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'w') as f:
    f.write(css)

print("Cleaned remnants")
