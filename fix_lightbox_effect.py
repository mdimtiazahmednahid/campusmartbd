import re

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'r') as f:
    js = f.read()

old_img_style = '''            // Image
            const bigImg = document.createElement('img');
            bigImg.src = imgSrc;
            bigImg.style.maxWidth = '90%';
            bigImg.style.maxHeight = '70vh';
            bigImg.style.objectFit = 'contain';
            bigImg.style.borderRadius = '16px';
            bigImg.style.boxShadow = '0 25px 50px -12px rgba(0, 0, 0, 0.5)';
            bigImg.style.transform = 'scale(0.9)';
            bigImg.style.transition = 'transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)';'''

new_img_style = '''            // Image
            const bigImg = document.createElement('img');
            bigImg.src = imgSrc;
            bigImg.style.maxWidth = '90%';
            bigImg.style.maxHeight = '70vh';
            bigImg.style.objectFit = 'contain';
            bigImg.style.borderRadius = '16px';
            bigImg.style.filter = 'drop-shadow(0 25px 35px rgba(0,0,0,0.6))';
            bigImg.style.transform = 'scale(0.9)';
            bigImg.style.transition = 'transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)';
            
            // Add float animation keyframes via a class if possible, or directly via inline animation if defined in CSS.
            // float is defined in style.css!
            bigImg.style.animation = 'float 6s ease-in-out infinite';
            bigImg.style.animationPlayState = 'paused'; // pause until scaled in'''

js = js.replace(old_img_style, new_img_style)

old_anim_trigger = '''            // Trigger animation
            requestAnimationFrame(() => {
                overlay.style.opacity = '1';
                bigImg.style.transform = 'scale(1)';
            });'''

new_anim_trigger = '''            // Trigger animation
            requestAnimationFrame(() => {
                overlay.style.opacity = '1';
                bigImg.style.transform = 'scale(1)';
                setTimeout(() => {
                    bigImg.style.animationPlayState = 'running';
                }, 300); // start float after pop-in
            });'''

js = js.replace(old_anim_trigger, new_anim_trigger)

with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'w') as f:
    f.write(js)
print("Added float and drop-shadow to lightbox image")
