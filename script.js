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

    
    // Hero Slideshow
    const heroImage = document.getElementById('hero-image');
    if (heroImage) {
        const slideImages = [
            'assets/kiloroad-black.png',
            'assets/kiloroad-navy.png',
            'assets/kiloroad-white.png',
            'assets/sust-blue.png',
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
            const tShirtType = item.tShirtType || 'Not Selected';
            const sizeMap = {
                'M': 'M (Chest-38, Length-27)',
                'L': 'L (Chest-40, Length-28)',
                'XL': 'XL (Chest-42, Length-29)',
                'XXL': 'XXL (Chest-44, Length-30)',
                '3XL': '3XL (Chest-46, Length-31)'
            };
            const detailedSize = sizeMap[item.size] || item.size;
            orderDetailsStr += `${item.title} (${tShirtType}, Size: ${detailedSize}) x${item.quantity} - ৳${effectivePrice * item.quantity}
`;

            const itemEl = document.createElement('div');
            itemEl.className = 'cart-item';
            itemEl.innerHTML = `
                <img src="${item.image}" alt="${item.title}">
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.title}</div>
                    <div class="cart-item-meta">${item.tShirtType || "Not Selected"}, Size: ${item.size}</div>
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
            
            const id = addBtn.getAttribute('data-id');
            const sizeSelect = document.getElementById(`size-${id}`);
            
            if (!card.dataset.basePrice) {
                card.dataset.basePrice = addBtn.getAttribute('data-price');
            }
            
            let basePrice = parseInt(card.dataset.basePrice);
            let additionalCost = 0;
            
            if (sizeSelect && (sizeSelect.value === 'XXL' || sizeSelect.value === '3XL')) {
                additionalCost = 50;
            }
            
            const newPrice = basePrice + additionalCost;
            
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
        
        const sizeSelect = document.getElementById(`size-${id}`);
        const typeSelect = document.getElementById(`type-${id}`);
        
        const size = sizeSelect ? sizeSelect.value : '';
        const tShirtType = typeSelect ? typeSelect.value : '';

        if (!size || !tShirtType) {
            alert('Please select a Size and T-shirt Type before adding to cart.');
            return;
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
            // Generate PDF Receipt Download
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();
            
            const orderDetails = formData.get('order_details');
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
            doc.text("CUSTOMER DETAILS", 20, 40);
            
            doc.setFontSize(11);
            doc.setFont(undefined, 'normal');
            doc.text(`Name: ${name}`, 20, 50);
            doc.text(`Phone: ${phone}`, 20, 58);
            doc.text(`Delivery Option: ${delivery}`, 20, 66);
            
            const splitAddress = doc.splitTextToSize(`Address: ${address}`, 170);
            doc.text(splitAddress, 20, 74);
            
            let currentY = 74 + (splitAddress.length * 7) + 5;
            
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
        if (savedVal && savedVal !== 'undefined' && savedVal !== 'null') {
            input.value = savedVal;
        } else {
            input.value = '';
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
