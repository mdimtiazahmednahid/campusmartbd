document.addEventListener('DOMContentLoaded', () => {
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
    });

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
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Cart State
    let cart = JSON.parse(localStorage.getItem('campusmart_cart')) || [];
    let isEarlyBirds = localStorage.getItem('campusmart_coupon') === 'EARLYBIRDS';

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

    // Update Cart UI & Data
    const updateCart = () => {
        // Save to LocalStorage immediately so empty arrays are saved before any early returns
        localStorage.setItem('campusmart_cart', JSON.stringify(cart));

        // Update count
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        cartCountElement.textContent = totalItems;

        // Render items
        cartItemsContainer.innerHTML = '';
        
        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<p style="text-align:center; color:#6b7280; margin-top:2rem;">Your cart is empty.</p>';
            cartTotalPrice.textContent = '৳ 0';
            orderDetailsInput.value = '';
            totalAmountInput.value = '0';
            return;
        }

        let total = 0;
        let orderDetailsStr = '';
        
        let discountPerItem = isEarlyBirds ? 51 : 0; // Reduces 550 to 499

        if (isEarlyBirds) {
            couponInput.value = 'EARLYBIRDS';
            couponMessage.textContent = 'EARLYBIRDS applied! ৳ 51 off per item.';
            couponMessage.className = 'coupon-message success';
        } else {
            couponMessage.textContent = '';
        }

        cart.forEach((item, index) => {
            const effectivePrice = item.price - discountPerItem;
            total += effectivePrice * item.quantity;
            orderDetailsStr += `${item.title} (Size: ${item.size}) x${item.quantity} - ৳${effectivePrice * item.quantity}\n`;

            const itemEl = document.createElement('div');
            itemEl.className = 'cart-item';
            itemEl.innerHTML = `
                <img src="${item.image}" alt="${item.title}">
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.title}</div>
                    <div class="cart-item-meta">Size: ${item.size}</div>
                    <div class="cart-item-price">৳ ${effectivePrice} ${isEarlyBirds ? '<del style="font-size:0.75rem;color:#9ca3af;margin-left:0.25rem;">৳ '+item.price+'</del>' : ''}</div>
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

        cartTotalPrice.textContent = `৳ ${total}`;
        
        // Update Netlify Form hidden inputs
        orderDetailsInput.value = orderDetailsStr;
        totalAmountInput.value = total;
        
        // Update advance amount for customization
        const advanceAmountSpan = document.getElementById('advance-amount');
        if (advanceAmountSpan) {
            advanceAmountSpan.textContent = `৳ ${Math.ceil(total / 2)}`;
        }
        if (hiddenCouponCodeInput) {
            hiddenCouponCodeInput.value = isEarlyBirds ? 'EARLYBIRDS' : '';
        }

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

    // Coupon Logic
    applyCouponBtn.addEventListener('click', () => {
        const code = couponInput.value.trim().toUpperCase();
        if (code === 'EARLYBIRDS') {
            isEarlyBirds = true;
            localStorage.setItem('campusmart_coupon', 'EARLYBIRDS');
            updateCart();
        } else if (code === '') {
            isEarlyBirds = false;
            localStorage.removeItem('campusmart_coupon');
            updateCart();
        } else {
            isEarlyBirds = false;
            localStorage.removeItem('campusmart_coupon');
            updateCart(); 
            // set error message after updateCart clears it
            couponMessage.textContent = 'Invalid coupon code';
            couponMessage.className = 'coupon-message error';
        }
    });

    // Dynamic Pricing based on Size
    // E.g. XXL size adds 50 BDT to the base price
    document.querySelectorAll('.size-select').forEach(select => {
        select.addEventListener('change', (e) => {
            const card = e.target.closest('.product-card');
            const priceElement = card.querySelector('.current-price');
            const addBtn = card.querySelector('.btn-add-cart');
            const buyBtn = card.querySelector('.btn-buy-now');
            
            // Assuming base price is what is initially set, let's read it or assume 450 for Kiloroad, 400 for Red Sustverse
            // Better to pull from data attribute. If not set, initialize it.
            if (!card.dataset.basePrice) {
                card.dataset.basePrice = addBtn.getAttribute('data-price');
            }
            
            let basePrice = parseInt(card.dataset.basePrice);
            let additionalCost = 0;
            
            // Add 50 BDT for XXL size
            if (e.target.value === 'XXL') {
                additionalCost = 50;
            }
            
            const newPrice = basePrice + additionalCost;
            
            // Update UI and Button data attributes
            priceElement.textContent = `৳ ${newPrice}`;
            addBtn.setAttribute('data-price', newPrice);
            buyBtn.setAttribute('data-price', newPrice);
        });
    });

    // Add to Cart Logic
    const handleAddToCart = (btn, openAfter = false) => {
        const id = btn.getAttribute('data-id');
        const title = btn.getAttribute('data-title');
        const price = parseInt(btn.getAttribute('data-price'));
        const image = btn.getAttribute('data-image');
        
        // Get size
        const sizeSelect = document.getElementById(`size-${id}`);
        const size = sizeSelect ? sizeSelect.value : 'M';

        // Check if item already exists in cart with same size
        const existingItemIndex = cart.findIndex(item => item.id === id && item.size === size);
        
        if (existingItemIndex > -1) {
            cart[existingItemIndex].quantity++;
        } else {
            cart.push({ id, title, price, image, size, quantity: 1 });
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
        
        if (cart.length === 0) {
            alert('Your cart is empty. Please add items before checking out.');
            return;
        }

        const submitBtn = checkoutForm.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.textContent;
        submitBtn.textContent = 'Processing...';
        submitBtn.disabled = true;

        const formData = new FormData(checkoutForm);
        
        fetch('/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams(formData).toString()
        })
        .then(() => {
            // Show toast
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);

            // Reset UI and state
            cart = [];
            isEarlyBirds = false;
            localStorage.removeItem('campusmart_coupon');
            if (couponInput) couponInput.value = '';
            updateCart();
            // We intentionally don't clear the form inputs so the address stays for next time
            closeCart();
        })
        .catch((error) => {
            alert('There was an issue submitting your order. Please try again.');
        })
        .finally(() => {
            submitBtn.textContent = originalBtnText;
            submitBtn.disabled = false;
        });
    });

    // Hero Image Slider
    const heroImages = [
        'assets/kiloroad-white.png',
        'assets/sust-blue.png',
        'assets/kiloroad-black.png'
    ];
    let currentHeroIndex = 0;
    const heroImageEl = document.getElementById('hero-image');

    if (heroImageEl) {
        setInterval(() => {
            heroImageEl.classList.add('fade-out');
            
            setTimeout(() => {
                currentHeroIndex = (currentHeroIndex + 1) % heroImages.length;
                heroImageEl.src = heroImages[currentHeroIndex];
                heroImageEl.classList.remove('fade-out');
            }, 500); // Wait for transition duration
        }, 4000); // Change image every 4 seconds
    }

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
        districtSelect.innerHTML = '<option value="">Select District</option>';
        
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
    });

    // Persist Checkout Form Data
    const formInputs = checkoutForm.querySelectorAll('input:not([type="hidden"]), textarea, select');
    formInputs.forEach(input => {
        // Load existing data if available
        const savedVal = localStorage.getItem(`campusmart_user_${input.name}`);
        if (savedVal) {
            input.value = savedVal;
        }

        // Save on input/change
        input.addEventListener('change', (e) => {
            localStorage.setItem(`campusmart_user_${e.target.name}`, e.target.value);
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
        districtSelect.innerHTML = '<option value="">Select District</option>';
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
    updateCart();
});
