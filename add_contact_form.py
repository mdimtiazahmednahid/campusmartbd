import re

# 1. Update HTML
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

old_contact = r'''            <div class="footer-contact">
                <h3>Contact Us</h3>
                <p><a href="tel:\+8801600265376" style="color: #9ca3af; transition: color 0\.3s ease;">📞 \+880
                        1600-265376</a></p>
                <p><a href="mailto:campusmartbd@gmail\.com" style="color: #9ca3af; transition: color 0\.3s ease;">✉️
                        campusmartbd@gmail\.com</a></p>
            </div>'''

new_contact = r'''            <div class="footer-contact">
                <h3>Contact Us</h3>
                <p><a href="tel:+8801600265376" style="color: #9ca3af; transition: color 0.3s ease;">📞 +880
                        1600-265376</a></p>
                <p><a href="mailto:campusmartbd@gmail.com" style="color: #9ca3af; transition: color 0.3s ease;">✉️
                        campusmartbd@gmail.com</a></p>
                <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="footer-contact-form">
                    <input type="hidden" name="form-name" value="contact">
                    <input type="text" name="name" placeholder="Your Name" required>
                    <input type="email" name="email" placeholder="Your Email" required>
                    <textarea name="message" placeholder="Your Message" rows="2" required></textarea>
                    <button type="submit" class="btn btn-submit-contact">Send Message</button>
                </form>
            </div>'''

html = re.sub(old_contact, new_contact, html)
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)

# 2. Add CSS
css_str = r'''
/* Footer Contact Form */
.footer-contact-form {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1rem;
    width: 100%;
}
.footer-contact-form input,
.footer-contact-form textarea {
    padding: 0.6rem;
    border-radius: 4px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    font-family: var(--font-main);
    font-size: 0.85rem;
    background: rgba(255, 255, 255, 0.05);
    color: white;
    outline: none;
    transition: border-color 0.3s ease;
}
.footer-contact-form input:focus,
.footer-contact-form textarea:focus {
    border-color: #f97316;
}
.footer-contact-form input::placeholder,
.footer-contact-form textarea::placeholder {
    color: rgba(255, 255, 255, 0.4);
}
.footer-contact-form .btn-submit-contact {
    background: linear-gradient(to right, #ea580c, #f97316);
    color: white;
    border: none;
    padding: 0.6rem;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
    font-size: 0.9rem;
}
.footer-contact-form .btn-submit-contact:hover {
    box-shadow: 0 4px 15px rgba(234, 88, 12, 0.4);
}
'''
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'a') as f:
    f.write(css_str)

print("Added Footer Contact Form")
