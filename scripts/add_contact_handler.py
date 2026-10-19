with open('/Users/MacBookPro/Downloads/CampusMartBD/script.js', 'a') as f:
    f.write('''

// Contact Form AJAX Handler
const contactForm = document.querySelector('.main-contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
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
''')

print("Added Contact Form AJAX Handler")
