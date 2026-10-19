import re

# 1. Update HTML
with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'r') as f:
    html = f.read()

# Remove form from footer
footer_contact_form = r'''                <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="footer-contact-form">
                    <input type="hidden" name="form-name" value="contact">
                    <input type="text" name="name" placeholder="Your Name" required>
                    <input type="email" name="email" placeholder="Your Email" required>
                    <textarea name="message" placeholder="Your Message" rows="2" required></textarea>
                    <button type="submit" class="btn btn-submit-contact">Send Message</button>
                </form>'''

html = html.replace(footer_contact_form, '')

# Inject new section
new_section = r'''        <section id="contact-us" class="contact-section">
            <div class="container">
                <div class="section-header">
                    <h2>Contact Us</h2>
                    <p>Have any questions? Send us a message.</p>
                </div>
                <div class="contact-form-wrapper">
                    <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="main-contact-form">
                        <input type="hidden" name="form-name" value="contact">
                        <div class="form-row">
                            <input type="text" name="name" placeholder="Your Name" required>
                            <input type="email" name="email" placeholder="Your Email" required>
                        </div>
                        <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
                        <button type="submit" class="btn btn-submit-contact">Send Message</button>
                    </form>
                </div>
            </div>
        </section>'''

html = html.replace('</section>\n    </main>', '</section>\n\n' + new_section + '\n    </main>')

with open('/Users/MacBookPro/Downloads/CampusMartBD/index.html', 'w') as f:
    f.write(html)

# 2. Update CSS
css_str = r'''
/* Main Contact Section */
.contact-section {
    padding: 5rem 0;
    background-color: var(--section-bg);
}
.contact-form-wrapper {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 2.5rem;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
}
.main-contact-form {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
}
.main-contact-form .form-row {
    display: flex;
    gap: 1.25rem;
}
.main-contact-form input,
.main-contact-form textarea {
    width: 100%;
    padding: 0.85rem;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    font-family: var(--font-main);
    font-size: 1rem;
    outline: none;
    transition: all 0.3s ease;
    background: #f9fafb;
}
.main-contact-form input:focus,
.main-contact-form textarea:focus {
    border-color: #f97316;
    background: white;
    box-shadow: 0 0 0 4px rgba(249, 115, 22, 0.1);
}
.main-contact-form .btn-submit-contact {
    background: linear-gradient(to right, #ea580c, #f97316);
    color: white;
    border: none;
    padding: 1rem;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.main-contact-form .btn-submit-contact:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(234, 88, 12, 0.4);
}
@media (max-width: 768px) {
    .main-contact-form .form-row {
        flex-direction: column;
    }
    .contact-form-wrapper {
        padding: 1.5rem;
    }
}
'''
with open('/Users/MacBookPro/Downloads/CampusMartBD/style.css', 'a') as f:
    f.write(css_str)

print("Moved contact form")
