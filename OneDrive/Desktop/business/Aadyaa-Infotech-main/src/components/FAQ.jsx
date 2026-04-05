import React, { useState } from 'react';

const FAQ = () => {
    const [activeIndex, setActiveIndex] = useState(null);

    const faqs = [
        {
            question: "How much does a website cost in Ahmedabad?",
            answer: "Website costs vary based on complexity. A basic business website starts from ₹15,000, e-commerce sites from ₹35,000, and custom web applications from ₹75,000. We provide free quotes based on your specific requirements. Contact us for a detailed estimate!"
        },
        {
            question: "How long does it take to build a website?",
            answer: "A simple website takes 5-7 working days, e-commerce websites take 10-15 days, and complex web applications can take 20-30 days or more. We always provide a clear timeline before starting the project and deliver on time."
        },
        {
            question: "Do you provide ongoing support after launch?",
            answer: "Yes! We provide 24/7 support for all our clients. This includes technical support, security updates, bug fixes, and content updates. We offer various maintenance packages starting from ₹2,000/month."
        },
        {
            question: "Can you redesign my existing website?",
            answer: "Absolutely! We specialize in website redesigns. We'll analyze your current site, identify areas for improvement, and create a modern, faster, and more effective version that ranks better on Google and converts more visitors into customers."
        },
        {
            question: "Do you offer payment plans or installments?",
            answer: "Yes, we offer flexible payment options. Typically, we work on a 50% advance and 50% on completion basis. For larger projects, we can split payments into milestones (e.g., 40% advance, 30% mid-project, 30% on delivery)."
        },
        {
            question: "Will my website be mobile-friendly?",
            answer: "100% Yes! All our websites are fully responsive and mobile-first designed. They look and work perfectly on all devices - desktops, laptops, tablets, and smartphones. Mobile optimization is crucial for SEO and user experience."
        },
        {
            question: "Do you provide SEO services?",
            answer: "Yes! We provide complete SEO services including keyword research, on-page optimization, technical SEO, content creation, and link building. We can optimize your website to rank on Google's first page for relevant searches."
        },
        {
            question: "What technologies do you use?",
            answer: "We use modern technologies like React.js, Node.js, WordPress, Shopify, and custom PHP solutions. For mobile apps, we develop in Android, iOS, and cross-platform frameworks like Flutter and React Native."
        },
        {
            question: "Are you only serving Ahmedabad clients?",
            answer: "While we're based in Ahmedabad, we work with clients across India and internationally. Thanks to remote collaboration tools, we successfully deliver projects to clients in Mumbai, Delhi, Bangalore, Dubai, USA, and more."
        },
        {
            question: "Can I update my website myself after it's built?",
            answer: "Yes! We build websites with user-friendly admin panels that allow you to update content, images, products, and blogs easily. We also provide training and documentation so you can manage your website confidently."
        }
    ];

    return (
        <section className="faq-section">
            <div className="container">
                <h2 className="section-title">Frequently Asked Questions</h2>
                <p className="section-subtitle">Get answers to common questions about our services</p>

                <div className="faq-container">
                    {faqs.map((faq, index) => (
                        <div 
                            className={`faq-item ${activeIndex === index ? 'active' : ''}`} 
                            key={index}
                            onClick={() => setActiveIndex(activeIndex === index ? null : index)}
                        >
                            <div className="faq-question">
                                <h3>{faq.question}</h3>
                                <i className={`fas fa-chevron-${activeIndex === index ? 'up' : 'down'}`}></i>
                            </div>
                            <div className="faq-answer">
                                <p>{faq.answer}</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default FAQ;
