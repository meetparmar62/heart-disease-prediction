import React, { useState } from 'react';
import emailjs from '@emailjs/browser';

const Contact = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        service: '',
        message: ''
    });
    
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [submitMessage, setSubmitMessage] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.id]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const { name, email, phone, service, message } = formData;

        if (!name || !email || !phone || !service || !message) {
            alert('Please fill in all fields');
            return;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address');
            return;
        }

        setIsSubmitting(true);

        try {
            // Initialize EmailJS with your public key
            await emailjs.init("u-JhSeC6Bnw5i2XoA");

            // Send email notification
            await emailjs.send(
                'service_w0f17wb',
                'YOUR_TEMPLATE_ID',
                {
                    from_name: name,
                    from_email: email,
                    phone: phone,
                    service: service,
                    message: message,
                    to_email: 'aadyaainfotech@gmail.com',
                    reply_to: email
                }
            );

            // Save inquiry to localStorage (for admin panel)
            const newInquiry = {
                name: name,
                contact: `${email} | ${phone}`,
                service: service,
                message: message,
                date: new Date().toISOString(),
                status: 'new'
            };

            const existingInquiries = JSON.parse(localStorage.getItem('inquiries') || '[]');
            existingInquiries.push(newInquiry);
            localStorage.setItem('inquiries', JSON.stringify(existingInquiries));

            // Track conversion
            const conversions = JSON.parse(localStorage.getItem('conversions') || '[]');
            conversions.push({
                type: 'contact_form',
                data: newInquiry,
                timestamp: new Date().toISOString()
            });
            localStorage.setItem('conversions', JSON.stringify(conversions));

            setSubmitMessage('Thank you! Your message has been sent successfully. We will contact you soon.');
            setFormData({ name: '', email: '', phone: '', service: '', message: '' });

            setTimeout(() => {
                setSubmitMessage('');
            }, 5000);

        } catch (error) {
            console.error('Error sending email:', error);
            
            // Fallback to WhatsApp if email fails
            const text = `*New Inquiry from Website*\n\n` +
                `*Name:* ${name}\n` +
                `*Email:* ${email}\n` +
                `*Phone:* ${phone}\n` +
                `*Service:* ${service}\n` +
                `*Message:* ${message}`;

            const whatsappURL = `https://wa.me/916355893624?text=${encodeURIComponent(text)}`;
            window.location.href = whatsappURL;
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <section id="contact" className="contact">
            <div className="container">
                <h2 className="section-title">Get In Touch</h2>
                <p className="section-subtitle">Ready to start your digital journey? Contact us today!</p>

                <div className="marquee-background">
                    <div className="marquee-inner">
                        {[...Array(10)].map((_, i) => (
                            <span key={i}>SPECIAL OFFER • WEB + APP + SEO = 4999 • </span>
                        ))}
                    </div>
                </div>

                <div className="contact-content">
                    <div className="contact-info">
                        <div className="contact-item">
                            <a href="https://wa.me/916355893624" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none', color: 'inherit', display: 'flex', alignItems: 'center', gap: '10px' }}>
                                <i className="fas fa-phone-alt"></i>
                                <div>
                                    <h4>WhatsApp</h4>
                                    <p>+91 63558 93624</p>
                                </div>
                            </a>
                        </div>

                        <div className="contact-item">
                            <a href="mailto:aadyaainfotech@gmail.com" style={{ textDecoration: 'none', color: 'inherit', display: 'flex', alignItems: 'center', gap: '10px' }}>
                                <i className="fas fa-envelope"></i>
                                <div>
                                    <h4>Email</h4>
                                    <p>aadyaainfotech@gmail.com</p>
                                </div>
                            </a>
                        </div>

                        <div className="contact-item">
                            <i className="fas fa-map-marker-alt"></i>
                            <div>
                                <h4>Location</h4>
                                <p>Ahmedabad, Gujarat, India</p>
                            </div>
                        </div>

                        <div className="social-links">
                            <a href="https://www.facebook.com/share/1AhUFCfrv7/" target="_blank" rel="noopener noreferrer" className="social-link facebook">
                                <i className="fab fa-facebook"></i>
                            </a>
                            <a href="https://www.linkedin.com/company/aadyaa-infotech" target="_blank" rel="noopener noreferrer" className="social-link linkedin">
                                <i className="fab fa-linkedin"></i>
                            </a>
                            <a href="https://www.instagram.com/aadyaa_infotech" target="_blank" rel="noopener noreferrer" className="social-link instagram">
                                <i className="fab fa-instagram"></i>
                            </a>
                            <a href="https://wa.me/916355893624" target="_blank" rel="noopener noreferrer" className="social-link whatsapp">
                                <i className="fab fa-whatsapp"></i>
                            </a>
                        </div>
                    </div>

                    <div className="contact-form">
                        {submitMessage && (
                            <div className="success-message" style={{
                                background: 'rgba(16, 185, 129, 0.1)',
                                border: '1px solid rgba(16, 185, 129, 0.3)',
                                padding: '1rem',
                                borderRadius: '8px',
                                marginBottom: '1rem',
                                color: '#10b981'
                            }}>
                                {submitMessage}
                            </div>
                        )}
                        <form id="contactForm" onSubmit={handleSubmit}>
                            <div className="form-group">
                                <input type="text" id="name" required placeholder="Your Name" value={formData.name} onChange={handleChange} disabled={isSubmitting} />
                            </div>
                            <div className="form-group">
                                <input type="email" id="email" required placeholder="Your Email" value={formData.email} onChange={handleChange} disabled={isSubmitting} />
                            </div>
                            <div className="form-group">
                                <input type="tel" id="phone" required placeholder="Your Phone Number" value={formData.phone} onChange={handleChange} disabled={isSubmitting} />
                            </div>
                            <div className="form-group">
                                <select id="service" required value={formData.service} onChange={handleChange} disabled={isSubmitting}>
                                    <option value="">Select Service</option>
                                    <option value="Website Development">Website Development</option>
                                    <option value="App Development">App Development</option>
                                    <option value="SEO (Search Engine Optimization)">SEO (Search Engine Optimization)</option>
                                    <option value="Digital Marketing">Digital Marketing</option>
                                    <option value="Social Media Management">Social Media Management</option>
                                    <option value="Branding & Design">Branding & Design</option>
                                    <option value="AI Automation">AI Automation</option>
                                </select>
                            </div>
                            <div className="form-group">
                                <textarea id="message" rows="5" required placeholder="Your Message" value={formData.message} onChange={handleChange} disabled={isSubmitting}></textarea>
                            </div>
                            <button type="submit" className="btn btn-primary btn-full" disabled={isSubmitting}>
                                {isSubmitting ? 'Sending...' : 'Send Message'}
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Contact;
