// Suppress / Dismiss "Powered by Netlify" Badge & Injected Drawer
try {
    localStorage.setItem('nl-hud:public:v1', JSON.stringify({ dismissed: true, hidden: true, state: 'hidden' }));
} catch (e) {}

if (typeof MutationObserver !== 'undefined') {
    const netlifyBadgeObserver = new MutationObserver((mutations) => {
        const netlifyWidgets = document.querySelectorAll('iframe[src*="netlify"], [data-netlify-badge], netlify-drawer, #netlify-drawer, div[id*="netlify-hud"]');
        if (netlifyWidgets.length > 0) {
            netlifyWidgets.forEach(el => el.remove());
        }
    });
    if (document.body) {
        netlifyBadgeObserver.observe(document.body, { childList: true, subtree: true });
    } else {
        document.addEventListener('DOMContentLoaded', () => {
            netlifyBadgeObserver.observe(document.body, { childList: true, subtree: true });
        });
    }
}

// Sweatshirts are offered in M, L, XL, 2XL (measurements in inches)
const sweatshirtSizeMap = {
    'M': 'M (Chest-39, Length-28)',
    'L': 'L (Chest-41, Length-29)',
    'XL': 'XL (Chest-43, Length-30)',
    '2XL': '2XL (Chest-45, Length-31)'
};
const jerseyPoloSizeMap = {
    'M': 'M (Chest-38, Length-27)',
    'L': 'L (Chest-40, Length-28)',
    'XL': 'XL (Chest-42, Length-29)',
    'XXL': 'XXL (Chest-44, Length-30)',
    '3XL': '3XL (Chest-46, Length-31)'
};
function isSweatshirtTitle(title) {
    const t = (title || '').toLowerCase();
    return t.includes('sweatshirt') || t.includes('quarter-zip');
}
function isPoloTitle(title) {
    const t = (title || '').toLowerCase();
    return t.includes('exclusive polo');
}
function isJacketTitle(title) {
    const t = (title || '').toLowerCase();
    return t.includes('jacket');
}
function isJerseyTitle(title) {
    return !isSweatshirtTitle(title) && !isPoloTitle(title) && !isJacketTitle(title);
}

// Toast Notification System

function showToast(message, type = 'error') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    const icon = type === 'error' ? '⚠️' : '✅';
    toast.innerHTML = `<span style="font-size: 1.2rem;">${icon}</span> <span>${message}</span>`;

    container.appendChild(toast);

    setTimeout(() => toast.classList.add('show'), 10);

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Error Reporting to Netlify Forms
function reportError(message, actionContext) {
    const formData = new URLSearchParams();
    formData.append('form-name', 'error-report');
    formData.append('error_message', message);
    formData.append('user_action', actionContext);

    fetch('/', {
        method: 'POST',
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData.toString()
    }).catch(err => console.error('Error reporting failed', err));
}

document.addEventListener('DOMContentLoaded', () => {

    function checkCampusAvailability() {
        const divisionSelect = document.getElementById('division');
        const districtSelect = document.getElementById('district');
        const insideCampusRadio = document.querySelector('input[value="Inside Campus"]');
        const outsideCampusRadio = document.querySelector('input[value="Outside Campus"]');
        const insideCampusLabel = insideCampusRadio.closest('label');

        if (divisionSelect.value === 'Sylhet' && districtSelect.value === 'Sylhet') {
            insideCampusRadio.disabled = false;
            insideCampusLabel.style.display = 'flex';
        } else {
            insideCampusRadio.disabled = true;
            insideCampusLabel.style.display = 'none';

            if (insideCampusRadio.checked) {
                outsideCampusRadio.checked = true;
                document.getElementById('outside-campus-msg').style.display = 'block';
            }
        }
    }

    // BD Location Data
    const bdLocations = {
        "Dhaka": ["Dhaka", "Faridpur", "Gazipur", "Gopalganj", "Kishoreganj", "Madaripur", "Manikganj", "Munshiganj", "Narayanganj", "Narsingdi", "Rajbari", "Shariatpur", "Tangail"],
        "Chattogram": ["Bandarban", "Brahmanbaria", "Chandpur", "Chattogram", "Cumilla", "Cox's Bazar", "Feni", "Khagrachari", "Lakshmipur", "Noakhali", "Rangamati"],
        "Rajshahi": ["Bogura", "Joypurhat", "Naogaon", "Natore", "Chapainawabganj", "Pabna", "Rajshahi", "Sirajganj"],
        "Khulna": ["Bagerhat", "Chuadanga", "Jashore", "Jhenaidah", "Khulna", "Kushtia", "Magura", "Meherpur", "Narail", "Satkhira"],
        "Barishal": ["Barguna", "Barishal", "Bhola", "Jhalokati", "Patuakhali", "Pirojpur"],
        "Sylhet": ["Habiganj", "Moulvibazar", "Sunamganj", "Sylhet"],
        "Rangpur": ["Dinajpur", "Gaibandha", "Kurigram", "Lalmonirhat", "Nilphamari", "Panchagarh", "Rangpur", "Thakurgaon"],
        "Mymensingh": ["Jamalpur", "Mymensingh", "Netrokona", "Sherpur"]
    };

    // Header scroll effect
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }, { passive: true });

    // Delivery Option Toggle
    const deliveryOptions = document.querySelectorAll('input[name="delivery_option"]');
    const outsideCampusMsg = document.getElementById('outside-campus-msg');

    deliveryOptions.forEach(option => {
        option.addEventListener('change', (e) => {
            if (e.target.value === 'Outside Campus') {
                outsideCampusMsg.style.display = 'block';
            } else {
                outsideCampusMsg.style.display = 'none';
            }
            updateCart();
        });
    });

    // Customization Toggle
    const isCustomizedCheckbox = document.getElementById('is_customized');
    const customizationDetails = document.getElementById('customization-details');
    const advanceAmountSpan = document.getElementById('advance-amount');

    if (isCustomizedCheckbox && customizationDetails) {
        isCustomizedCheckbox.addEventListener('change', (e) => {
            if (e.target.checked) {
                customizationDetails.style.display = 'block';
                // Make required fields required
                document.querySelector('input[name="custom_name"]').required = true;
                document.querySelector('input[name="custom_number"]').required = true;
                document.querySelector('input[name="sender_number"]').required = true;
            } else {
                customizationDetails.style.display = 'none';
                // Remove required attribute
                document.querySelector('input[name="custom_name"]').required = false;
                document.querySelector('input[name="custom_number"]').required = false;
                document.querySelector('input[name="sender_number"]').required = false;
            }
        });
    }

    // Copy bKash/Nagad Number
    const copyBtn = document.getElementById('copy-number-btn');
    const copyToast = document.getElementById('copy-toast');
    if (copyBtn && copyToast) {
        copyBtn.addEventListener('click', () => {
            navigator.clipboard.writeText('+8801600265376').then(() => {
                copyToast.style.display = 'block';
                setTimeout(() => {
                    copyToast.style.display = 'none';
                }, 2000);
            });
        });
    }

    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navMenu = document.getElementById('nav-menu');

    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                navMenu.classList.remove('active');
            }
        });
    }



    // Hero Slideshow
    const heroImage = document.getElementById('hero-image');
    if (heroImage) {
        const slideImages = [
            'assets/kiloroad-black.webp',
            'assets/kiloroad-navy.webp',
            'assets/kiloroad-white.webp',
            'assets/sust-blue.webp',
            'assets/sustverse-red.webp',
            'assets/sustverse-grey.webp',
            'assets/sust-polo-black.webp',
            'assets/sust-sweatshirt-coffee.webp'
        ];
        let currentSlide = 0;

        setInterval(() => {
            heroImage.classList.add('fade-out');
            setTimeout(() => {
                currentSlide = (currentSlide + 1) % slideImages.length;
                heroImage.src = slideImages[currentSlide];
                heroImage.classList.remove('fade-out');
            }, 500);
        }, 3500);
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - headerHeight;
                const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
                window.scrollTo({
                    top: targetPosition,
                    behavior: prefersReducedMotion ? 'auto' : 'smooth'
                });
            }
        });
    });

    // OCG Department Coupon State (5% discount — only active when explicitly applied in current session)
    let isOcgCoupon = false;
    try {
        localStorage.removeItem('campusmart_coupon');
        localStorage.removeItem('campusmart_user_');
    } catch (e) {}

    // Cart State
    // A corrupted/blocked localStorage entry must never break the whole page
    let cart = [];
    try {
        const storedCart = JSON.parse(localStorage.getItem('campusmart_cart'));
        if (Array.isArray(storedCart)) {
            cart = storedCart
                .filter(item => !isJacketTitle(item.title) && String(item.id) !== '10')
                .map(item => {
                    // Migrate legacy .png image paths and legacy prices if any exist in localStorage
                    if (item.image && item.image.endsWith('.png')) {
                        item.image = item.image.replace(/\.png$/, '.webp');
                    }
                    if (isSweatshirtTitle(item.title)) {
                        item.price = 630;
                    } else if (isPoloTitle(item.title)) {
                        item.price = 550;
                    } else if (isJerseyTitle(item.title)) {
                        item.price = item.tShirtType === 'Polo Collar + full sleeve' ? 530 : 499;
                    }
                    return item;
                });
        }
    } catch (e) {
        cart = [];
    }

    // DOM Elements
    const cartIcon = document.getElementById('cart-icon');
    const cartOverlay = document.getElementById('cart-overlay');
    const cartSidebar = document.getElementById('cart-sidebar');
    const closeCartBtn = document.getElementById('close-cart');
    const cartCountElement = document.querySelector('.cart-count');
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalPrice = document.getElementById('cart-total-price');
    const orderDetailsInput = document.getElementById('order_details');
    const totalAmountInput = document.getElementById('total_amount');
    const hiddenCouponCodeInput = document.getElementById('hidden_coupon_code');
    const checkoutForm = document.getElementById('checkout-form');

    // Coupon Elements
    const couponInput = document.getElementById('coupon-code');
    const applyCouponBtn = document.getElementById('apply-coupon');
    const couponMessage = document.getElementById('coupon-message');

    // Toggle Cart Sidebar
    const openCart = () => {
        cartSidebar.classList.add('active');
        cartOverlay.classList.add('active');
    };

    const closeCart = () => {
        cartSidebar.classList.remove('active');
        cartOverlay.classList.remove('active');
    };

    cartIcon.addEventListener('click', openCart);
    closeCartBtn.addEventListener('click', closeCart);
    cartOverlay.addEventListener('click', closeCart);

    // Keyboard accessibility: Enter/Space opens the cart, Escape closes it
    cartIcon.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            openCart();
        }
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && cartSidebar.classList.contains('active')) closeCart();
    });

    // Update Cart UI & Data
    const updateCart = () => {
        // Save to LocalStorage immediately so empty arrays are saved before any early returns
        try {
            localStorage.setItem('campusmart_cart', JSON.stringify(cart));
        } catch (e) {}

        // Update count
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        cartCountElement.textContent = totalItems;

        // Render items
        cartItemsContainer.innerHTML = '';

        if (cart.length === 0) {
            cartItemsContainer.innerHTML = `
                <div style="text-align:center; padding: 3rem 1rem; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
                    <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5" style="margin-bottom: 1.5rem;">
                        <circle cx="9" cy="21" r="1"></circle>
                        <circle cx="20" cy="21" r="1"></circle>
                        <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                    </svg>
                    <h4 style="font-size: 1.3rem; color: #1e293b; margin-bottom: 0.5rem; font-weight: 700;">Your Cart is Empty</h4>
                    <p style="color: #64748b; margin-bottom: 2rem; font-size: 0.95rem;">Looks like you haven't added any items yet.</p>
                    <button onclick="document.getElementById('close-cart').click()" style="background: #3b82f6; color: white; border: none; padding: 0.8rem 1.8rem; border-radius: 12px; font-weight: 600; cursor: pointer; transition: transform 0.1s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(59,130,246,0.3);" onmousedown="this.style.transform='scale(0.96)'" onmouseup="this.style.transform='scale(1)'" onmouseleave="this.style.transform='scale(1)'">Browse Collection</button>
                </div>
            `;
            cartTotalPrice.textContent = '৳ 0';
            const subtotalElement = document.getElementById('cart-subtotal-price');
            const deliveryChargeElement = document.getElementById('cart-delivery-price');
            const discountRowElement = document.getElementById('cart-discount-row');
            if (subtotalElement) subtotalElement.textContent = '৳ 0';
            if (deliveryChargeElement) deliveryChargeElement.textContent = '৳ 0';
            if (discountRowElement) discountRowElement.style.display = 'none';
            if (couponMessage) {
                couponMessage.textContent = '';
                couponMessage.style.display = 'none';
            }
            if (couponInput) couponInput.value = '';
            isOcgCoupon = false;
            orderDetailsInput.value = '';
            totalAmountInput.value = '0';
            checkoutForm.style.display = 'none'; // Hide checkout form if cart is empty
            return;
        } else {
            checkoutForm.style.display = 'block';
        }

        let orderDetailsStr = '';

        // Calculate Delivery Charge
        let deliveryCharge = 0;
        const isInsideCampus = document.querySelector('input[name="delivery_option"]:checked')?.value === 'Inside Campus';
        const district = document.getElementById('district').value;

        let outsideChargeText = "৳110 - ৳130";
        if (district === 'Dhaka' || district === 'Sylhet') {
            outsideChargeText = "৳110";
        } else if (district) {
            outsideChargeText = "৳130";
        }

        const dynamicChargeEl = document.getElementById('dynamic-outside-charge');
        if (dynamicChargeEl) {
            dynamicChargeEl.textContent = outsideChargeText;
        }

        if (!isInsideCampus) {
            if (district === 'Dhaka' || district === 'Sylhet') {
                deliveryCharge = 110;
            } else if (district) {
                deliveryCharge = 130;
            } else {
                deliveryCharge = 130; // Default to 130 if not selected yet but outside campus
            }
        }

        let subtotal = 0;

        cart.forEach((item, index) => {
            const isSweatshirt = isSweatshirtTitle(item.title);
            const isPolo = isPoloTitle(item.title);
            const isJacket = isJacketTitle(item.title);

            // Ensure Jersey price reflects Polo Collar + full sleeve (530) vs others (499)
            if (!isSweatshirt && !isPolo && !isJacket) {
                item.price = item.tShirtType === 'Polo Collar + full sleeve' ? 530 : 499;
            }

            const effectivePrice = item.price;
            subtotal += effectivePrice * item.quantity;
            const tShirtType = item.tShirtType || 'Not Selected';
            const sizeMap = isSweatshirt ? sweatshirtSizeMap : jerseyPoloSizeMap;
            const detailedSize = sizeMap[item.size] || item.size;
            orderDetailsStr += `${item.title} (${tShirtType}, Size: ${detailedSize}) x${item.quantity} - ৳${effectivePrice * item.quantity}
`;

            let typeOptionsHtml = '';
            if (isPolo) {
                typeOptionsHtml = `
                    <option value="">Type</option>
                    <option value="Lacoste Polo (Half Sleeve)" ${item.tShirtType === 'Lacoste Polo (Half Sleeve)' ? 'selected' : ''}>Lacoste Polo (Half)</option>
                `;
            } else if (isSweatshirt) {
                typeOptionsHtml = `
                    <option value="">Style</option>
                    <option value="High Neck Quarter-Zip" ${(item.tShirtType === 'High Neck Quarter-Zip' || item.tShirtType === 'Quarter-Zip Pullover') ? 'selected' : ''}>High Neck Quarter-Zip</option>
                `;
            } else if (isJacket) {
                typeOptionsHtml = `
                    <option value="">Style</option>
                    <option value="Fleece Winter Edition" ${item.tShirtType === 'Fleece Winter Edition' ? 'selected' : ''}>Fleece Winter</option>
                    <option value="Bonded Windproof Edition" ${item.tShirtType === 'Bonded Windproof Edition' ? 'selected' : ''}>Bonded Windproof</option>
                    <option value="Thermal Winter Edition" ${item.tShirtType === 'Thermal Winter Edition' ? 'selected' : ''}>Thermal Winter</option>
                `;
            } else {
                typeOptionsHtml = `
                    <option value="">Type</option>
                    <option value="Polo Collar + half sleeve" ${item.tShirtType === 'Polo Collar + half sleeve' ? 'selected' : ''}>Polo + Half (৳499)</option>
                    <option value="Polo Collar + full sleeve" ${item.tShirtType === 'Polo Collar + full sleeve' ? 'selected' : ''}>Polo + Full (৳530)</option>
                    <option value="Round Collar + half sleeve" ${item.tShirtType === 'Round Collar + half sleeve' ? 'selected' : ''}>Round + Half (৳499)</option>
                    <option value="Round Collar + full sleeve" ${item.tShirtType === 'Round Collar + full sleeve' ? 'selected' : ''}>Round + Full (৳499)</option>
                `;
            }

            const itemEl = document.createElement('div');
            itemEl.className = 'cart-item';

            itemEl.innerHTML = `
                <img src="${item.image}" alt="${item.title}">
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.title}</div>
                    <div class="cart-item-options" style="display:flex; gap:0.5rem; margin-top:0.25rem;">
                        <select class="cart-size-select" data-index="${index}" style="padding:0.25rem; font-size:0.8rem; border-radius:4px; border:1px solid var(--border-color); width:48%; background:white; cursor:pointer; outline:none; ${(item.size === '' && document.getElementById('checkout-form').classList.contains('submitted')) ? 'border-color: #dc2626; box-shadow: 0 0 0 1px #dc2626;' : ''}">
                            <option value="">Size</option>
                            ${isSweatshirt ? `
                            <option value="M" ${item.size === 'M' ? 'selected' : ''}>${sweatshirtSizeMap['M']}</option>
                            <option value="L" ${item.size === 'L' ? 'selected' : ''}>${sweatshirtSizeMap['L']}</option>
                            <option value="XL" ${item.size === 'XL' ? 'selected' : ''}>${sweatshirtSizeMap['XL']}</option>
                            <option value="2XL" ${item.size === '2XL' ? 'selected' : ''}>${sweatshirtSizeMap['2XL']}</option>
                            ` : `
                            <option value="M" ${item.size === 'M' ? 'selected' : ''}>M (Chest-38, Length-27)</option>
                            <option value="L" ${item.size === 'L' ? 'selected' : ''}>L (Chest-40, Length-28)</option>
                            <option value="XL" ${item.size === 'XL' ? 'selected' : ''}>XL (Chest-42, Length-29)</option>
                            <option value="XXL" ${item.size === 'XXL' ? 'selected' : ''}>XXL (Chest-44, Length-30)</option>
                            <option value="3XL" ${item.size === '3XL' ? 'selected' : ''}>3XL (Chest-46, Length-31)</option>
                            `}
                        </select>
                        <select class="cart-type-select" data-index="${index}" style="padding:0.25rem; font-size:0.8rem; border-radius:4px; border:1px solid var(--border-color); width:48%; background:white; cursor:pointer; outline:none; ${(item.tShirtType === '' && document.getElementById('checkout-form').classList.contains('submitted')) ? 'border-color: #dc2626; box-shadow: 0 0 0 1px #dc2626;' : ''}">
                            ${typeOptionsHtml}
                        </select>
                    </div>
                    <div class="cart-item-price" style="margin-top:0.5rem;">৳ ${effectivePrice}</div>
                    <div class="cart-item-actions">
                        <button class="qty-btn minus" data-index="${index}">-</button>
                        <span>${item.quantity}</span>
                        <button class="qty-btn plus" data-index="${index}">+</button>
                        <button class="remove-item" data-index="${index}">Remove</button>
                    </div>
                </div>
            `;
            cartItemsContainer.appendChild(itemEl);
        });

        const discountAmount = isOcgCoupon ? Math.round(subtotal * 0.05) : 0;
        const discountedSubtotal = Math.max(0, subtotal - discountAmount);
        const finalTotal = discountedSubtotal + deliveryCharge;

        const subtotalElement = document.getElementById('cart-subtotal-price');
        const discountRowElement = document.getElementById('cart-discount-row');
        const discountPriceElement = document.getElementById('cart-discount-price');
        const deliveryChargeElement = document.getElementById('cart-delivery-price');

        if (subtotalElement) subtotalElement.textContent = `৳ ${subtotal}`;
        if (discountRowElement && discountPriceElement) {
            if (isOcgCoupon && discountAmount > 0) {
                discountRowElement.style.display = 'flex';
                discountPriceElement.textContent = `- ৳ ${discountAmount}`;
            } else {
                discountRowElement.style.display = 'none';
            }
        }
        if (couponMessage) {
            if (isOcgCoupon) {
                couponMessage.textContent = `Coupon applied! 5% discount (-৳${discountAmount}) added.`;
                couponMessage.className = 'coupon-message success';
                couponMessage.style.display = 'block';
            } else {
                couponMessage.textContent = '';
                couponMessage.style.display = 'none';
            }
        }
        if (deliveryChargeElement) deliveryChargeElement.textContent = `৳ ${deliveryCharge}`;

        cartTotalPrice.textContent = `৳ ${finalTotal}`;

        if (isOcgCoupon && discountAmount > 0) {
            orderDetailsStr += `\nCoupon Discount (OCG - 5%): -৳${discountAmount}`;
        }

        // Add delivery info to order details
        if (deliveryCharge > 0) {
            orderDetailsStr += `\nDelivery Charge: ৳${deliveryCharge}`;
        } else {
            orderDetailsStr += `\nDelivery Charge: Free`;
        }

        // Update Netlify Form hidden inputs
        orderDetailsInput.value = orderDetailsStr;
        totalAmountInput.value = finalTotal;
        if (hiddenCouponCodeInput) {
            hiddenCouponCodeInput.value = isOcgCoupon ? 'OCG' : '';
        }

        // Update advance amount for customization (50% of total including delivery)
        const advanceAmountSpan = document.getElementById('advance-amount');
        if (advanceAmountSpan) {
            advanceAmountSpan.textContent = `৳ ${Math.ceil(finalTotal / 2)}`;
        }

        // Add event listeners to the variant selectors
        document.querySelectorAll('.cart-size-select').forEach(select => {
            select.addEventListener('change', (e) => {
                const idx = e.target.getAttribute('data-index');
                cart[idx].size = e.target.value;
                document.getElementById('checkout-form').classList.remove('submitted');
                updateCart();
            });
        });

        document.querySelectorAll('.cart-type-select').forEach(select => {
            select.addEventListener('change', (e) => {
                const idx = e.target.getAttribute('data-index');
                const newType = e.target.value;
                cart[idx].tShirtType = newType;
                if (isJerseyTitle(cart[idx].title)) {
                    cart[idx].price = newType === 'Polo Collar + full sleeve' ? 530 : 499;
                }
                document.getElementById('checkout-form').classList.remove('submitted');
                updateCart();
            });
        });

        // Add event listeners to newly created buttons
        document.querySelectorAll('.qty-btn.minus').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const idx = e.target.getAttribute('data-index');
                if (cart[idx].quantity > 1) {
                    cart[idx].quantity--;
                } else {
                    cart.splice(idx, 1);
                }
                updateCart();
            });
        });

        document.querySelectorAll('.qty-btn.plus').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const idx = e.target.getAttribute('data-index');
                cart[idx].quantity++;
                updateCart();
            });
        });

        document.querySelectorAll('.remove-item').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const idx = e.target.getAttribute('data-index');
                cart.splice(idx, 1);
                updateCart();
            });
        });
    };

    // Coupon Logic (OCG -> 5% discount, only when user types and clicks Apply)
    if (applyCouponBtn && couponInput) {
        couponInput.value = '';
        const handleApplyCoupon = () => {
            const code = couponInput.value.trim().toUpperCase();
            if (code === 'OCG') {
                isOcgCoupon = true;
                updateCart();
            } else if (code === '') {
                isOcgCoupon = false;
                updateCart();
            } else {
                isOcgCoupon = false;
                updateCart();
                if (couponMessage) {
                    couponMessage.textContent = 'Invalid coupon code';
                    couponMessage.className = 'coupon-message error';
                    couponMessage.style.display = 'block';
                }
            }
        };

        applyCouponBtn.addEventListener('click', handleApplyCoupon);
        couponInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                handleApplyCoupon();
            }
        });
    }

    // Dynamic Pricing based on Jersey Type (Polo Collar + full sleeve -> ৳530, others -> ৳499)
    document.querySelectorAll('.type-select').forEach(select => {
        select.addEventListener('change', (e) => {
            const card = e.target.closest('.product-card');
            if (!card || card.dataset.productType !== 'jersey') return;

            const priceElement = card.querySelector('.current-price');
            const addBtn = card.querySelector('.btn-add-cart');
            const buyBtn = card.querySelector('.btn-buy-now');

            const newPrice = e.target.value === 'Polo Collar + full sleeve' ? 530 : 499;

            if (priceElement) priceElement.textContent = `৳ ${newPrice}`;
            if (addBtn) addBtn.setAttribute('data-price', newPrice);
            if (buyBtn) buyBtn.setAttribute('data-price', newPrice);
        });
    });

    // Multi-Image Gallery Pills on Product Cards (Design / Front / Back)
    document.querySelectorAll('.gallery-pill').forEach(pill => {
        pill.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const card = pill.closest('.product-card');
            if (!card) return;
            const img = card.querySelector('.product-image');
            const targetSrc = pill.getAttribute('data-img');
            if (img && targetSrc) {
                img.src = targetSrc;
            }
            card.querySelectorAll('.gallery-pill').forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
        });
    });

    // Add to Cart Logic
    const handleAddToCart = (btn, openAfter = false) => {
        const id = btn.getAttribute('data-id');
        const title = btn.getAttribute('data-title');
        const price = parseInt(btn.getAttribute('data-price'));
        const image = btn.getAttribute('data-image');

        // Find the closest product card to read the selected size and type
        const card = btn.closest('.product-card');
        let size = '';
        let tShirtType = '';
        if (card) {
            const sizeSelect = card.querySelector('select[id^="size-"]');
            const typeSelect = card.querySelector('select[id^="type-"]');
            if (sizeSelect && sizeSelect.value) size = sizeSelect.value;
            if (typeSelect && typeSelect.value) tShirtType = typeSelect.value;
        }

        const existingItemIndex = cart.findIndex(item => item.id === id && item.size === size && item.tShirtType === tShirtType);

        if (existingItemIndex > -1) {
            cart[existingItemIndex].quantity++;
        } else {
            cart.push({ id, title, price, image, size, tShirtType, quantity: 1 });
        }

        updateCart();

        // Animate cart icon
        cartIcon.style.transform = 'scale(1.2)';
        setTimeout(() => {
            cartIcon.style.transform = 'scale(1)';
        }, 200);

        if (openAfter) {
            openCart();
        } else {
            // Button feedback
            const originalText = btn.textContent;
            btn.textContent = 'Added!';
            btn.style.backgroundColor = '#10b981';
            btn.style.color = '#fff';

            setTimeout(() => {
                btn.textContent = originalText;
                btn.style.backgroundColor = '';
                btn.style.color = '';
            }, 1000);
        }
    };

    document.querySelectorAll('.btn-add-cart').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            handleAddToCart(e.target, false);
        });
    });

    document.querySelectorAll('.btn-buy-now').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            handleAddToCart(e.target, true);
        });
    });

    // Form submission intercept for empty cart validation and AJAX handling
    checkoutForm.addEventListener('submit', (e) => {
        e.preventDefault();

        checkoutForm.classList.add('submitted'); // Add class to trigger red borders on missing selects

        if (cart.length === 0) {
            showToast('Your cart is empty. Please add items before checking out.'); reportError('Attempted checkout with empty cart', 'checkout');
            return;
        }

        // Validate that all items have a size and type selected
        const unselectedItem = cart.find(item => !item.size || !item.tShirtType);
        if (unselectedItem) {
            showToast('Please select a Size and Type for all items in your cart.');
            reportError('Missing size/type at checkout', 'checkout');
            updateCart(); // Re-render to show red borders
            return;
        }

        const submitBtn = checkoutForm.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.textContent;
        submitBtn.textContent = 'Processing...';
        submitBtn.disabled = true;

        const formData = new FormData(checkoutForm);

        // Anti-Autofill Bug Fix: Explicitly grab and set values directly from the DOM
        const nameInput = checkoutForm.querySelector('[name="name"]');
        const phoneInput = checkoutForm.querySelector('[name="phone"]');
        const emailInput = checkoutForm.querySelector('[name="email"]');
        const institutionInput = checkoutForm.querySelector('[name="institution"]');
        const departmentInput = checkoutForm.querySelector('[name="department"]');
        const sessionInput = checkoutForm.querySelector('[name="session"]');

        if (nameInput) formData.set('name', nameInput.value);
        if (phoneInput) formData.set('phone', phoneInput.value);
        if (emailInput) formData.set('email', emailInput.value);
        if (institutionInput) formData.set('institution', institutionInput.value);
        if (departmentInput) formData.set('department', departmentInput.value);
        if (sessionInput) formData.set('session', sessionInput.value);

        const institutionVal = (institutionInput && institutionInput.value) ? institutionInput.value : 'N/A';
        const departmentVal = (departmentInput && departmentInput.value) ? departmentInput.value : 'N/A';
        const sessionVal = (sessionInput && sessionInput.value) ? sessionInput.value : 'N/A';

        // Include Academic Info inside order_details as well for complete Netlify visibility
        const baseOrderDetails = orderDetailsInput ? orderDetailsInput.value : '';
        const fullOrderDetails = `${baseOrderDetails}\nAcademic Info: Institution: ${institutionVal} | Dept: ${departmentVal} | Session: ${sessionVal}`;
        formData.set('order_details', fullOrderDetails);

        fetch('/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams(formData).toString()
        })
            .then(() => {
                // Generate PDF Receipt Download
                const { jsPDF } = window.jspdf;
                const doc = new jsPDF();

                const orderDetails = baseOrderDetails;
                const total = formData.get('total_amount');
                const name = formData.get('name');
                const phone = formData.get('phone');
                const delivery = formData.get('delivery_option');
                const address = `${formData.get('address') || ''}, ${formData.get('upazila') || ''}, ${formData.get('district') || ''}, ${formData.get('division') || ''}`;

                doc.setFontSize(20);
                doc.setFont(undefined, 'bold');
                doc.text("CAMPUSMART ORDER RECEIPT", 105, 20, null, null, "center");

                doc.setFontSize(12);
                doc.setFont(undefined, 'bold');
                doc.text("CUSTOMER & ACADEMIC DETAILS", 20, 40);

                doc.setFontSize(11);
                doc.setFont(undefined, 'normal');
                doc.text(`Name: ${name}`, 20, 50);
                doc.text(`Phone: ${phone}`, 20, 57);
                doc.text(`Institution: ${institutionVal}  |  Dept: ${departmentVal}  |  Session: ${sessionVal}`, 20, 64);
                doc.text(`Delivery Option: ${delivery}`, 20, 71);

                const splitAddress = doc.splitTextToSize(`Address: ${address}`, 170);
                doc.text(splitAddress, 20, 78);

                let currentY = 78 + (splitAddress.length * 7) + 5;

                doc.setFontSize(12);
                doc.setFont(undefined, 'bold');
                doc.text("ORDER ITEMS", 20, currentY);
                currentY += 10;

                doc.setFontSize(11);
                doc.setFont(undefined, 'normal');
                const splitItems = doc.splitTextToSize(orderDetails, 170);
                doc.text(splitItems, 20, currentY);
                currentY += (splitItems.length * 7) + 5;

                doc.setFontSize(14);
                doc.setFont(undefined, 'bold');
                doc.text(`Total Amount: Tk ${total}`, 20, currentY);
                currentY += 15;

                if (formData.get('is_customized') === 'on') {
                    doc.setFontSize(12);
                    doc.setFont(undefined, 'bold');
                    doc.text("CUSTOMIZATION DETAILS", 20, currentY);
                    currentY += 10;

                    doc.setFontSize(11);
                    doc.setFont(undefined, 'normal');
                    doc.text(`Name on Jersey: ${formData.get('custom_name')}`, 20, currentY);
                    doc.text(`Number on Jersey: ${formData.get('custom_number')}`, 20, currentY + 8);
                    doc.text(`Advance Paid via bKash/Nagad`, 20, currentY + 16);
                    doc.text(`Sender Number: ${formData.get('sender_number')}`, 20, currentY + 24);
                    doc.text(`TrxID: ${formData.get('trx_id') || 'N/A'}`, 20, currentY + 32);
                    currentY += 45;
                }

                doc.setFontSize(12);
                doc.setFont(undefined, 'italic');
                doc.text("Thank you for shopping with CampusMart!", 105, currentY, null, null, "center");

                doc.save(`CampusMart_Order_${Date.now()}.pdf`);

                // Build WhatsApp Message First
                let waMsg = `*NEW ORDER - CAMPUSMART*\n---------------------\n`;
                waMsg += `*Customer Details:*\nName: ${name}\nPhone: ${phone}\n`;
                if (formData.get('email')) waMsg += `Email: ${formData.get('email')}\n`;

                waMsg += `\n*Academic Info:*\nInstitution: ${institutionVal}\nDepartment: ${departmentVal}\nSession: ${sessionVal}\n`;

                waMsg += `\n*Delivery:*\nOption: ${delivery}\n`;
                if (address.replace(/,/g, '').trim()) waMsg += `Address: ${address}\n`;

                waMsg += `\n*Order Summary:*\n`;
                let imageUrls = [];
                cart.forEach(item => {
                    const sizeMap = isSweatshirtTitle(item.title) ? sweatshirtSizeMap : jerseyPoloSizeMap;
                    const fullSize = sizeMap[item.size] || item.size || 'N/A';
                    waMsg += `- ${item.title} (${item.tShirtType || 'N/A'}, Size: ${fullSize}) x${item.quantity} (৳${item.price * item.quantity})\n`;
                    if (item.image) {
                        try {
                            imageUrls.push(new URL(item.image, window.location.href).href);
                        } catch (e) { }
                    }
                });

                if (formData.get('is_customized') === 'on') {
                    waMsg += `\n*Customization:*\nName: ${formData.get('custom_name')}\nNumber: ${formData.get('custom_number')}\n`;
                    waMsg += `Advance: Paid\n`;
                    waMsg += `bKash/Nagad No: ${formData.get('sender_number')}\nTrxID: ${formData.get('trx_id')}\n`;
                    waMsg += `_Note: Customization (May take 7-15 working days to prepare)_\n`;
                }

                const totalStr = document.getElementById('cart-total-price').textContent;
                if (formData.get('coupon_code')) {
                    waMsg += `\n*Coupon Applied:* ${formData.get('coupon_code')} (5% Discount)\n`;
                }
                waMsg += `\n*Total Bill:* ${totalStr}\n`;

                // Append product image link so WhatsApp automatically generates an image preview thumbnail
                if (imageUrls.length > 0) {
                    waMsg += `\n*Product Image Reference:*\n${imageUrls[0]}\n`;
                }

                const encodedWaMsg = encodeURIComponent(waMsg);
                const whatsappUrl = `https://wa.me/8801600265376?text=${encodedWaMsg}`;

                // Save to Order History with URL
                const orderInfo = {
                    date: new Date().toLocaleString(),
                    items: cart.map(item => `${item.title} (${item.quantity}x)`).join(', '),
                    total: totalStr,
                    waUrl: whatsappUrl
                };
                const history = JSON.parse(localStorage.getItem('campusMartHistory')) || [];
                history.push(orderInfo);
                localStorage.setItem('campusMartHistory', JSON.stringify(history));

                // Show toast
                const toast = document.getElementById('toast');
                toast.classList.add('show');
                setTimeout(() => {
                    toast.classList.remove('show');
                }, 3000);

                // Reset UI and state
                cart = [];
                isOcgCoupon = false;
                localStorage.removeItem('campusmart_coupon');
                if (couponInput) couponInput.value = '';

                updateCart();
                // We intentionally don't clear the form inputs so the address stays for next time
                closeCart();

                // Show WhatsApp Prompt Modal
                const waModal = document.createElement('div');
                waModal.style.cssText = "position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(15,23,42,0.8); backdrop-filter:blur(10px); z-index:99999; display:flex; justify-content:center; align-items:center; opacity:0; transition:opacity 0.3s ease;";

                waModal.innerHTML = `
                <div style="background:#ffffff; padding:2.5rem; border-radius:24px; text-align:center; max-width:400px; width:90%; box-shadow:0 25px 50px -12px rgba(0,0,0,0.25); transform:scale(0.9); transition:transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);">
                    <div style="width:64px; height:64px; background:#10b981; border-radius:50%; display:flex; justify-content:center; align-items:center; margin:0 auto 1.5rem auto;">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    </div>
                    <h2 style="font-size:1.5rem; color:#0f172a; margin-bottom:0.75rem; font-weight:800;">Order Request Received!</h2>
                    <p style="color:#64748b; font-size:0.95rem; margin-bottom:0.75rem; line-height:1.5;">Your order request has been received. Our team will check the availability of your selected product and contact you shortly to confirm your order.</p>
                    <p style="color:#64748b; font-size:0.95rem; margin-bottom:1.75rem; line-height:1.5;">For faster processing and a quicker response, please send your order details to us on WhatsApp.</p>
                    <a href="${whatsappUrl}" target="_blank" style="display:flex; justify-content:center; align-items:center; gap:0.5rem; background:#25D366; color:white; text-decoration:none; padding:1rem; border-radius:14px; font-weight:700; font-size:1.1rem; margin-bottom:1rem; box-shadow:0 4px 15px rgba(37,211,102,0.3); transition:transform 0.2s;" onmousedown="this.style.transform='scale(0.96)'" onmouseup="this.style.transform='scale(1)'">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                        Send to WhatsApp
                    </a>
                    <button id="close-wa-modal" style="background:transparent; color:#94a3b8; border:none; font-weight:600; font-size:0.9rem; cursor:pointer; padding:0.5rem;">Maybe later</button>
                </div>
            `;
                document.body.appendChild(waModal);

                setTimeout(() => {
                    waModal.style.opacity = '1';
                    waModal.children[0].style.transform = 'scale(1)';
                }, 10);

                document.getElementById('close-wa-modal').addEventListener('click', () => {
                    waModal.style.opacity = '0';
                    waModal.children[0].style.transform = 'scale(0.9)';
                    setTimeout(() => waModal.remove(), 300);
                });

                // Auto close if they click the whatsapp link
                waModal.querySelector('a').addEventListener('click', () => {
                    setTimeout(() => {
                        waModal.style.opacity = '0';
                        waModal.children[0].style.transform = 'scale(0.9)';
                        setTimeout(() => waModal.remove(), 300);
                    }, 500);
                });
            })
            .catch((error) => {
                const container = document.getElementById('toast-container');
                if (container) {
                    const toast = document.createElement('div');
                    toast.className = `toast toast-error`;
                    const toastId = 'toast-' + Date.now();
                    toast.innerHTML = `<span style="font-size: 1.2rem;">⚠️</span> 
                                   <span style="display:flex; flex-direction:column; gap:0.5rem; width:100%;">
                                       <span>Order submission failed. Please try again.</span>
                                       <button id="btn-${toastId}" style="background:rgba(255,255,255,0.2); color:white; border:1px solid rgba(255,255,255,0.4); padding:0.4rem 0.8rem; border-radius:6px; cursor:pointer; font-weight:600; font-size:0.8rem; transition:all 0.2s; align-self:flex-start;">Send Error Report</button>
                                   </span>`;
                    container.appendChild(toast);
                    setTimeout(() => toast.classList.add('show'), 10);

                    const btn = document.getElementById(`btn-${toastId}`);
                    if (btn) {
                        btn.addEventListener('click', (e) => {
                            e.target.textContent = 'Sending...';
                            e.target.style.opacity = '0.7';
                            reportError('Order submission failed', 'form_submit');
                            setTimeout(() => {
                                e.target.textContent = 'Report Sent!';
                                e.target.style.background = 'rgba(16, 185, 129, 0.3)';
                                e.target.style.borderColor = 'rgba(16, 185, 129, 0.8)';
                                e.target.style.opacity = '1';
                            }, 800);
                        });
                    }

                    setTimeout(() => {
                        toast.classList.remove('show');
                        setTimeout(() => toast.remove(), 300);
                    }, 6000);
                }
            })
            .finally(() => {
                submitBtn.textContent = originalBtnText;
                submitBtn.disabled = false;
            });
    });

    // Division and District Logic
    const divisionSelect = document.getElementById('division');
    const districtSelect = document.getElementById('district');

    // Populate Divisions
    Object.keys(bdLocations).forEach(div => {
        const option = document.createElement('option');
        option.value = div;
        option.textContent = div;
        divisionSelect.appendChild(option);
    });

    // Handle Division Change
    divisionSelect.addEventListener('change', (e) => {
        const selectedDiv = e.target.value;
        districtSelect.innerHTML = '<option value="">Select District *</option>';

        if (selectedDiv && bdLocations[selectedDiv]) {
            districtSelect.disabled = false;
            bdLocations[selectedDiv].forEach(dist => {
                const option = document.createElement('option');
                option.value = dist;
                option.textContent = dist;
                districtSelect.appendChild(option);
            });
        } else {
            districtSelect.disabled = true;
        }
        checkCampusAvailability();
        updateCart();
    });

    districtSelect.addEventListener('change', (e) => {
        checkCampusAvailability();
        updateCart();
    });

    // Persist Checkout Form Data
    const formInputs = checkoutForm.querySelectorAll('input:not([type="hidden"]):not(#coupon-code), textarea, select');
    formInputs.forEach(input => {
        // Load existing data if available
        const savedVal = localStorage.getItem(`campusmart_user_${input.name}`);
        if (savedVal && savedVal !== 'undefined' && savedVal !== 'null') {
            if (input.type === 'radio') {
                if (input.value === savedVal) {
                    input.checked = true;
                }
            } else if (input.type === 'checkbox') {
                input.checked = savedVal === 'true';
            } else {
                input.value = savedVal;
            }
        } else if (input.type !== 'radio' && input.type !== 'checkbox') {
            input.value = '';
        }

        // Save on input/change
        input.addEventListener('change', (e) => {
            if (e.target.type === 'checkbox') {
                localStorage.setItem(`campusmart_user_${e.target.name}`, e.target.checked);
            } else {
                localStorage.setItem(`campusmart_user_${e.target.name}`, e.target.value);
            }
        });

        if (input.tagName === 'INPUT' || input.tagName === 'TEXTAREA') {
            input.addEventListener('input', (e) => {
                localStorage.setItem(`campusmart_user_${e.target.name}`, e.target.value);
            });
        }
    });

    // Handle District dropdown initialization on page load if Division was saved
    const savedDivision = divisionSelect.value;
    if (savedDivision && bdLocations[savedDivision]) {
        districtSelect.innerHTML = '<option value="">Select District *</option>';
        districtSelect.disabled = false;
        bdLocations[savedDivision].forEach(dist => {
            const option = document.createElement('option');
            option.value = dist;
            option.textContent = dist;
            districtSelect.appendChild(option);
        });
        // Re-apply saved district now that options exist
        const savedDistrict = localStorage.getItem('campusmart_user_district');
        if (savedDistrict) {
            districtSelect.value = savedDistrict;
        }
    }

    // Initial render
    checkCampusAvailability();
    updateCart();
});


// Contact Form AJAX Handler
const contactForm = document.querySelector('.main-contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new URLSearchParams(new FormData(contactForm));

        const btn = contactForm.querySelector('button[type="submit"]');
        const originalText = btn.textContent;
        btn.textContent = 'Sending...';
        btn.disabled = true;

        fetch('/', {
            method: 'POST',
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: formData.toString()
        }).then(() => {
            showToast('Thanks for contacting us!', 'success');
            contactForm.reset();
        }).catch((error) => {
            showToast('Something went wrong. Please try again.', 'error');
        }).finally(() => {
            btn.textContent = originalText;
            btn.disabled = false;
        });
    });
}

// Order History Logic
const navHistory = document.getElementById('nav-history');
const historySidebar = document.getElementById('history-sidebar');
const historyOverlay = document.getElementById('history-overlay');
const closeHistory = document.getElementById('close-history');
const historyItems = document.getElementById('history-items');

function loadOrderHistory() {
    let history = [];
    try {
        const stored = localStorage.getItem('campusMartHistory');
        if (stored && stored !== 'undefined' && stored !== 'null') {
            history = JSON.parse(stored);
        }
    } catch (e) {
        console.error('Failed to parse history', e);
        history = [];
    }

    if (!Array.isArray(history)) {
        history = [];
    }

    historyItems.innerHTML = '';

    if (history.length === 0) {
        historyItems.innerHTML = '<div class="empty-cart"><p>You have no past orders.</p></div>';
        return;
    }

    history.slice().reverse().forEach(order => {
        let waLink = order.waUrl;
        if (!waLink) {
            // Fallback for older orders placed before the update
            const fallbackText = encodeURIComponent(`*PAST ORDER - CAMPUSMART*\nDate: ${order.date}\nItems: ${order.items}\nTotal: ${order.total}`);
            waLink = `https://wa.me/8801600265376?text=${fallbackText}`;
        }

        const item = document.createElement('div');
        item.className = 'history-item';
        item.style.position = 'relative';
        item.innerHTML = `
            <div class="history-date">${order.date}</div>
            <div class="history-title">${order.items}</div>
            <div class="history-total" style="margin-bottom: 0.5rem;">Total: ${order.total}</div>
            <a href="${waLink}" target="_blank" style="display:inline-flex; align-items:center; gap:0.25rem; font-size:0.75rem; background:#25D366; color:white; padding:0.3rem 0.6rem; border-radius:4px; font-weight:600; text-decoration:none;"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg> Forward to WhatsApp</a>
        `;
        historyItems.appendChild(item);
    });
}

function openHistory() {
    loadOrderHistory();
    historySidebar.classList.add('active');
    historyOverlay.classList.add('active');
}

function closeHistoryFn() {
    historySidebar.classList.remove('active');
    historyOverlay.classList.remove('active');
}

if (navHistory) {
    navHistory.addEventListener('click', (e) => {
        e.preventDefault();
        openHistory();
    });
}
if (closeHistory) closeHistory.addEventListener('click', closeHistoryFn);
if (historyOverlay) historyOverlay.addEventListener('click', closeHistoryFn);
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && historySidebar && historySidebar.classList.contains('active')) closeHistoryFn();
});


// =========================================
// Product Image Lightbox & Product Details Modal
// =========================================
document.addEventListener('DOMContentLoaded', () => {
    function parseGalleryAttr(card, fallbackSrc) {
        const raw = card ? card.getAttribute('data-gallery') : '';
        if (!raw) return [{ label: 'Photo', src: fallbackSrc }];
        return raw.split(',').map(pair => {
            const [label, src] = pair.split('|');
            return { label: (label || 'Photo').trim(), src: (src || fallbackSrc).trim() };
        }).filter(item => item.src);
    }

    document.querySelectorAll('.product-image-container img').forEach(img => {
        img.style.cursor = 'zoom-in';
        img.addEventListener('click', (e) => {
            const card = e.target.closest('.product-card');
            const buyBtn = card.querySelector('.btn-buy-now');
            const imgSrc = e.target.getAttribute('src') || e.target.src;
            const title = buyBtn.getAttribute('data-title');
            const price = buyBtn.getAttribute('data-price');
            const galleryItems = parseGalleryAttr(card, imgSrc);

            // Create Lightbox overlay
            const overlay = document.createElement('div');
            overlay.className = 'lightbox-overlay';
            overlay.style.position = 'fixed';
            overlay.style.top = '0';
            overlay.style.left = '0';
            overlay.style.width = '100vw';
            overlay.style.height = '100vh';
            overlay.style.backgroundColor = 'rgba(42, 4, 13, 0.95)';
            overlay.style.backdropFilter = 'blur(10px)';
            overlay.style.zIndex = '999999';
            overlay.style.display = 'flex';
            overlay.style.flexDirection = 'column';
            overlay.style.alignItems = 'center';
            overlay.style.justifyContent = 'center';
            overlay.style.opacity = '0';
            overlay.style.transition = 'opacity 0.3s ease';

            // Close Button
            const closeBtn = document.createElement('button');
            closeBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>';
            closeBtn.style.position = 'absolute';
            closeBtn.style.top = '20px';
            closeBtn.style.right = '20px';
            closeBtn.style.background = 'rgba(255,255,255,0.1)';
            closeBtn.style.border = 'none';
            closeBtn.style.color = 'white';
            closeBtn.style.width = '44px';
            closeBtn.style.height = '44px';
            closeBtn.style.borderRadius = '50%';
            closeBtn.style.cursor = 'pointer';
            closeBtn.style.display = 'flex';
            closeBtn.style.alignItems = 'center';
            closeBtn.style.justifyContent = 'center';
            closeBtn.style.transition = 'all 0.2s';
            closeBtn.onmouseover = () => closeBtn.style.background = 'rgba(255,255,255,0.2)';
            closeBtn.onmouseout = () => closeBtn.style.background = 'rgba(255,255,255,0.1)';

            // Image
            const bigImg = document.createElement('img');
            bigImg.src = imgSrc;
            bigImg.style.maxWidth = '90%';
            bigImg.style.maxHeight = '64vh';
            bigImg.style.objectFit = 'contain';
            bigImg.style.borderRadius = '16px';
            bigImg.style.filter = 'drop-shadow(0 25px 35px rgba(0,0,0,0.6))';
            bigImg.style.transform = 'scale(0.9)';
            bigImg.style.transition = 'transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)';
            bigImg.style.animation = 'float 6s ease-in-out infinite';
            bigImg.style.animationPlayState = 'paused';

            // Gallery Switcher Pills inside Lightbox (if multiple images)
            let switcherBar = null;
            if (galleryItems.length > 1) {
                switcherBar = document.createElement('div');
                switcherBar.style.cssText = 'display:flex; gap:0.5rem; margin-top:14px; background:rgba(255,255,255,0.12); padding:0.35rem; border-radius:999px;';
                galleryItems.forEach(item => {
                    const btn = document.createElement('button');
                    btn.type = 'button';
                    btn.textContent = item.label;
                    const isActive = imgSrc.endsWith(item.src);
                    btn.style.cssText = `border:none; padding:0.38rem 0.9rem; border-radius:999px; font-weight:700; font-size:0.82rem; cursor:pointer; transition:all 0.2s; background:${isActive ? '#ffffff' : 'transparent'}; color:${isActive ? '#9b1122' : '#ffffff'};`;
                    btn.onclick = () => {
                        bigImg.src = item.src;
                        Array.from(switcherBar.children).forEach(c => {
                            c.style.background = 'transparent';
                            c.style.color = '#ffffff';
                        });
                        btn.style.background = '#ffffff';
                        btn.style.color = '#9b1122';
                    };
                    switcherBar.appendChild(btn);
                });
            }

            // Text Details
            const details = document.createElement('div');
            details.style.color = 'white';
            details.style.textAlign = 'center';
            details.style.marginTop = '16px';
            details.innerHTML = `<h3 style="margin:0; font-size:1.4rem; font-weight:800; color:#ffffff;">${title}</h3><p style="color:#ff4d66; font-size:1.2rem; font-weight:700; margin:5px 0 14px;">৳ ${price}</p>`;

            // Order Request Action
            const actionBtn = document.createElement('button');
            actionBtn.textContent = 'Order Request';
            actionBtn.style.background = 'linear-gradient(135deg, #6c0a1a 0%, #9b1122 45%, #42040d 100%)';
            actionBtn.style.color = 'white';
            actionBtn.style.border = 'none';
            actionBtn.style.padding = '0.9rem 2.6rem';
            actionBtn.style.borderRadius = '12px';
            actionBtn.style.fontSize = '1.05rem';
            actionBtn.style.fontWeight = '700';
            actionBtn.style.cursor = 'pointer';
            actionBtn.style.boxShadow = '0 8px 24px rgba(108, 10, 26, 0.6)';
            actionBtn.onclick = () => {
                closeOverlay();
                buyBtn.click();
            };

            const closeOverlay = () => {
                overlay.style.opacity = '0';
                bigImg.style.transform = 'scale(0.9)';
                setTimeout(() => overlay.remove(), 300);
            };

            closeBtn.onclick = closeOverlay;
            overlay.onclick = (e) => {
                if (e.target === overlay) closeOverlay();
            };

            overlay.appendChild(closeBtn);
            overlay.appendChild(bigImg);
            if (switcherBar) overlay.appendChild(switcherBar);
            overlay.appendChild(details);
            details.appendChild(actionBtn);
            document.body.appendChild(overlay);

            // Trigger animation
            requestAnimationFrame(() => {
                overlay.style.opacity = '1';
                bigImg.style.transform = 'scale(1)';
                setTimeout(() => {
                    bigImg.style.animationPlayState = 'running';
                }, 300);
            });
        });
    });

    // =========================================
    // Product Details Modal (.btn-product-details)
    // =========================================
    function openProductDetailsModal(card) {
        if (!card) return;
        const addBtn = card.querySelector('.btn-add-cart');
        const buyBtn = card.querySelector('.btn-buy-now');
        const imgEl = card.querySelector('.product-image');
        const title = buyBtn ? buyBtn.getAttribute('data-title') : (card.querySelector('.product-title')?.textContent || 'Product Details');
        const currentImg = imgEl ? (imgEl.getAttribute('src') || imgEl.src) : '';
        const productType = card.getAttribute('data-product-type') || 'jersey';
        const detailsName = card.getAttribute('data-details-name') || 'SUST Exclusive Edition';
        const detailsFabric = card.getAttribute('data-details-fabric') || 'Premium Export Quality Fabric';
        const detailsPrice = card.getAttribute('data-details-price') || `৳${buyBtn ? buyBtn.getAttribute('data-price') : ''}`;
        const galleryItems = parseGalleryAttr(card, currentImg);

        const isSweatshirt = productType === 'sweatshirt' || isSweatshirtTitle(title);

        const sizeTableRows = isSweatshirt
            ? `
                <tr><td>M</td><td>39"</td><td>28"</td></tr>
                <tr><td>L</td><td>41"</td><td>29"</td></tr>
                <tr><td>XL</td><td>43"</td><td>30"</td></tr>
                <tr><td>2XL</td><td>45"</td><td>31"</td></tr>
            `
            : `
                <tr><td>M</td><td>38"</td><td>27"</td></tr>
                <tr><td>L</td><td>40"</td><td>28"</td></tr>
                <tr><td>XL</td><td>42"</td><td>29"</td></tr>
                <tr><td>XXL</td><td>44"</td><td>30"</td></tr>
                <tr><td>3XL</td><td>46"</td><td>31"</td></tr>
            `;

        const sizeChartHeading = isSweatshirt
            ? 'High Neck Sweatshirt Size Chart (Inches)'
            : 'Jersey & Polo T-Shirt Size Chart (Inches)';

        const modalOverlay = document.createElement('div');
        modalOverlay.className = 'product-details-modal-overlay';

        const thumbsHtml = galleryItems.length > 1
            ? `<div class="pdm-thumbs">
                ${galleryItems.map((g, idx) => `<button type="button" class="pdm-thumb-btn ${idx === 0 ? 'active' : ''}" data-src="${g.src}">${g.label}</button>`).join('')}
               </div>`
            : '';

        modalOverlay.innerHTML = `
            <div class="product-details-modal" role="dialog" aria-modal="true">
                <button type="button" class="pdm-close-btn" aria-label="Close Product Details">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6L6 18M6 6l12 12"/></svg>
                </button>
                <div class="pdm-image-viewer">
                    <img src="${galleryItems[0]?.src || currentImg}" alt="${title}" class="pdm-main-img">
                    ${thumbsHtml}
                </div>
                <span class="pdm-badge">${detailsName}</span>
                <h3 class="pdm-title">${title}</h3>
                <div class="pdm-specs">
                    <div class="pdm-spec-row">
                        <strong>Fabric:</strong>
                        <span>${detailsFabric}</span>
                    </div>
                    <div class="pdm-spec-row">
                        <strong>Price:</strong>
                        <span style="color:#9b1122; font-weight:700;">${detailsPrice}</span>
                    </div>
                </div>
                <h4 class="pdm-size-title">${sizeChartHeading}</h4>
                <table class="pdm-size-table">
                    <thead>
                        <tr><th>Size</th><th>Chest</th><th>Length</th></tr>
                    </thead>
                    <tbody>
                        ${sizeTableRows}
                    </tbody>
                </table>
                <div style="display:flex; gap:0.6rem;">
                    <button type="button" class="btn btn-add-cart pdm-add-btn" style="flex:1; height:42px; font-size:0.9rem; font-weight:700; border-radius:10px; cursor:pointer;">Add to Cart</button>
                    <button type="button" class="btn btn-buy-now pdm-order-btn" style="flex:1; height:42px; font-size:0.9rem; font-weight:700; border-radius:10px; cursor:pointer;">Order Request</button>
                </div>
            </div>
        `;

        const closeModal = () => {
            modalOverlay.classList.remove('active');
            setTimeout(() => modalOverlay.remove(), 250);
        };

        modalOverlay.querySelector('.pdm-close-btn').addEventListener('click', closeModal);
        modalOverlay.addEventListener('click', (e) => {
            if (e.target === modalOverlay) closeModal();
        });

        const mainImgEl = modalOverlay.querySelector('.pdm-main-img');
        modalOverlay.querySelectorAll('.pdm-thumb-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                mainImgEl.src = btn.getAttribute('data-src');
                modalOverlay.querySelectorAll('.pdm-thumb-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            });
        });

        modalOverlay.querySelector('.pdm-add-btn').addEventListener('click', () => {
            closeModal();
            if (addBtn) addBtn.click();
        });

        modalOverlay.querySelector('.pdm-order-btn').addEventListener('click', () => {
            closeModal();
            if (buyBtn) buyBtn.click();
        });

        document.body.appendChild(modalOverlay);
        requestAnimationFrame(() => modalOverlay.classList.add('active'));
    }

    document.querySelectorAll('.btn-product-details').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const card = btn.closest('.product-card');
            openProductDetailsModal(card);
        });
    });

    // ==========================================
    // STICKY CATEGORY FILTERING & NAVIGATION
    // ==========================================
    const categoryMetadata = {
        'all': {
            title: 'Latest Collection',
            subtitle: 'Explore our university editions and anticipated releases.',
            isLive: true
        },
        'campus-wear': {
            title: 'Campus Wear Collection',
            subtitle: 'Designed for campus life • University editions and student sportswear.',
            isLive: true
        },
        'essentials': {
            badge: 'Dropping Next',
            icon: '🎒',
            title: 'Student Essentials',
            subtitle: 'We are curating student essentials built around campus daily routine & academic life. First batch drops soon!',
            waText: "Hi CampusMart, I'm interested in pre-ordering Student Essentials!",
            isLive: false
        },
        'culture': {
            badge: 'Batch & Fest Merch',
            icon: '🎓',
            title: 'Campus Culture',
            subtitle: 'Campus fests, batch memorabilia, department identities, and university spirit wear.',
            waText: "Hi CampusMart, I'm interested in pre-ordering Campus Culture items!",
            isLive: false
        },
        'accessories': {
            badge: 'Campus Gear',
            icon: '⌚',
            title: 'Campus Gear & Accessories',
            subtitle: 'Smart daily utility gear, durable campus carry, and student accessories.',
            waText: "Hi CampusMart, I'm interested in pre-ordering Campus Gear!",
            isLive: false
        },
        'everyday': {
            title: 'Everyday & Winter Wear',
            subtitle: 'Exclusive polo t-shirts, quarter-zip sweatshirts, and comfortable fits built for campus life.',
            isLive: true
        }
    };

    function filterByCategory(category, shouldScroll = true) {
        // Update Sticky Category Buttons
        document.querySelectorAll('.sticky-cat-btn').forEach(btn => {
            if (btn.dataset.category === category) {
                btn.classList.add('active');
                btn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
            } else {
                btn.classList.remove('active');
            }
        });

        // Update Category Cards in Core Categories Section
        document.querySelectorAll('.category-card[data-category]').forEach(card => {
            if (card.dataset.category === category) {
                card.classList.add('active');
            } else {
                card.classList.remove('active');
            }
        });

        const collectionHeading = document.getElementById('collection-heading');
        const collectionSubheading = document.getElementById('collection-subheading');
        const productGrid = document.querySelector('.product-grid');
        const emptyState = document.getElementById('category-empty-state');
        const meta = categoryMetadata[category] || categoryMetadata['all'];

        if (meta.isLive) {
            // Live Category (all / campus-wear / everyday)
            if (collectionHeading) collectionHeading.textContent = meta.title;
            if (collectionSubheading) collectionSubheading.textContent = meta.subtitle;

            if (emptyState) emptyState.style.display = 'none';
            if (productGrid) {
                productGrid.style.display = 'grid';
                const productCards = productGrid.querySelectorAll('.product-card');
                productCards.forEach(card => {
                    const cardCats = (card.dataset.category || '').split(/\s+/);
                    if (category === 'all' || cardCats.includes(category)) {
                        card.style.display = 'flex';
                        card.style.animation = 'fadeInUp 0.35s ease forwards';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }
        } else {
            // Upcoming Category
            if (collectionHeading) collectionHeading.textContent = meta.title;
            if (collectionSubheading) collectionSubheading.textContent = 'Dropping Soon • Pre-Orders Open';

            if (productGrid) productGrid.style.display = 'none';
            if (emptyState) {
                emptyState.style.display = 'flex';
                const badgeEl = document.getElementById('empty-state-badge');
                const iconEl = document.getElementById('empty-state-icon');
                const titleEl = document.getElementById('empty-state-title');
                const subtitleEl = document.getElementById('empty-state-subtitle');
                const waBtn = document.getElementById('empty-state-wa-btn');

                if (badgeEl) badgeEl.textContent = meta.badge || 'Dropping Soon';
                if (iconEl) iconEl.textContent = meta.icon || '✨';
                if (titleEl) titleEl.textContent = meta.title;
                if (subtitleEl) subtitleEl.textContent = meta.subtitle;
                if (waBtn) {
                    waBtn.href = `https://wa.me/8801600265376?text=${encodeURIComponent(meta.waText || 'Hi CampusMart!')}`;
                }
            }
        }

        // Smooth scroll to collection section with header + sticky bar offset
        if (shouldScroll) {
            const collectionEl = document.getElementById('collection');
            if (collectionEl) {
                const headerEl = document.querySelector('.header');
                const stickyBarEl = document.getElementById('sticky-category-bar');
                const headerHeight = headerEl ? headerEl.offsetHeight : 80;
                const stickyHeight = stickyBarEl ? stickyBarEl.offsetHeight : 56;
                const offset = headerHeight + stickyHeight + 15;
                const targetPos = collectionEl.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({
                    top: Math.max(0, targetPos),
                    behavior: 'smooth'
                });
            }
        }
    }

    // Attach click handlers to Sticky Category Buttons
    document.querySelectorAll('.sticky-cat-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const cat = btn.dataset.category || 'all';
            filterByCategory(cat, true);
        });
    });

    // Attach click handlers to Category Cards
    document.querySelectorAll('.category-card[data-category]').forEach(card => {
        card.addEventListener('click', (e) => {
            e.preventDefault();
            const cat = card.dataset.category;
            if (cat) filterByCategory(cat, true);
        });
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const cat = card.dataset.category;
                if (cat) filterByCategory(cat, true);
            }
        });
    });

    // Button to switch back to Campus Wear from empty state
    const btnShowCampusWear = document.getElementById('btn-show-campus-wear');
    if (btnShowCampusWear) {
        btnShowCampusWear.addEventListener('click', () => {
            filterByCategory('campus-wear', true);
        });
    }

    // Explore Launch Wear CTA button
    const btnPromoExplore = document.getElementById('btn-promo-explore');
    if (btnPromoExplore) {
        btnPromoExplore.addEventListener('click', (e) => {
            e.preventDefault();
            filterByCategory('campus-wear', true);
        });
    }
});
