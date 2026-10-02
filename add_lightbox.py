import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

lightbox_logic = '''
    // =========================================
    // Product Image Lightbox (Click to Zoom)
    // =========================================
    document.querySelectorAll('.product-image-container img').forEach(img => {
        img.style.cursor = 'zoom-in';
        img.addEventListener('click', (e) => {
            const card = e.target.closest('.product-card');
            const buyBtn = card.querySelector('.btn-buy-now');
            const imgSrc = e.target.src;
            const title = buyBtn.getAttribute('data-title');
            const price = buyBtn.getAttribute('data-price');
            
            // Create Lightbox overlay
            const overlay = document.createElement('div');
            overlay.className = 'lightbox-overlay';
            overlay.style.position = 'fixed';
            overlay.style.top = '0';
            overlay.style.left = '0';
            overlay.style.width = '100vw';
            overlay.style.height = '100vh';
            overlay.style.backgroundColor = 'rgba(15, 23, 42, 0.95)';
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
            bigImg.style.maxHeight = '70vh';
            bigImg.style.objectFit = 'contain';
            bigImg.style.borderRadius = '16px';
            bigImg.style.boxShadow = '0 25px 50px -12px rgba(0, 0, 0, 0.5)';
            bigImg.style.transform = 'scale(0.9)';
            bigImg.style.transition = 'transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)';
            
            // Text Details
            const details = document.createElement('div');
            details.style.color = 'white';
            details.style.textAlign = 'center';
            details.style.marginTop = '20px';
            details.innerHTML = `<h3 style="margin:0; font-size:1.5rem; font-weight:800;">${title}</h3><p style="color:#f97316; font-size:1.25rem; font-weight:700; margin:5px 0 15px;">৳ ${price}</p>`;
            
            // Buy Now Action
            const actionBtn = document.createElement('button');
            actionBtn.textContent = 'Buy Now';
            actionBtn.style.background = 'linear-gradient(135deg, #ea580c 0%, #f97316 100%)';
            actionBtn.style.color = 'white';
            actionBtn.style.border = 'none';
            actionBtn.style.padding = '1rem 3rem';
            actionBtn.style.borderRadius = '12px';
            actionBtn.style.fontSize = '1.1rem';
            actionBtn.style.fontWeight = '700';
            actionBtn.style.cursor = 'pointer';
            actionBtn.style.boxShadow = '0 8px 20px rgba(234, 88, 12, 0.4)';
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
                if(e.target === overlay) closeOverlay();
            };
            
            overlay.appendChild(closeBtn);
            overlay.appendChild(bigImg);
            overlay.appendChild(details);
            details.appendChild(actionBtn);
            document.body.appendChild(overlay);
            
            // Trigger animation
            requestAnimationFrame(() => {
                overlay.style.opacity = '1';
                bigImg.style.transform = 'scale(1)';
            });
        });
    });
'''

# insert before "// Initialize on load"
insert_target = '// Initialize on load'
if insert_target in js:
    js = js.replace(insert_target, lightbox_logic + '\n    ' + insert_target)
    with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
        f.write(js)
    print("Added Lightbox logic successfully")
else:
    print("Could not find insert target")

