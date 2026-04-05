import React, { useEffect, useState } from 'react';

const defaultServices = [
    {
        title: "Website Development",
        icon: "fa-laptop-code",
        desc: "Professional website development services in Ahmedabad. Custom websites that work 24/7 to sell your services while you sleep. Fast, SEO-ready sites that convert visitors into customers. Serving clients across SG Highway, Satellite, Vastrapur, Bodakdev, and all areas in Ahmedabad.",
        features: [
            "Custom Website Development in Ahmedabad",
            "Business Website (Static & Dynamic)",
            "E-commerce Website Development",
            "Responsive Web Design",
            "Mobile-First Responsiveness",
            "Technical SEO Architecture",
            "Lightning Fast Page Loading",
            "WordPress Website Development",
            "Serving All Areas in Ahmedabad"
        ]
    },
    {
        title: "Application Development",
        icon: "fa-mobile-alt",
        desc: "Professional application development services in Ahmedabad. Put your business in your customers' pocket with native iOS and Android apps or cross-platform solutions that engage users. Trusted by businesses in Prahlad Nagar, Thaltej, Navrangpura, and throughout Ahmedabad.",
        features: [
            "Android App Development in Ahmedabad",
            "iOS App Development in Ahmedabad",
            "Cross-Platform App Development",
            "Service / Booking Apps",
            "Custom Business Applications",
            "Native App Development",
            "App Store Publishing Support",
            "React Native App Development",
            "Available Across Ahmedabad"
        ]
    },
    {
        title: "SEO (Search Engine Optimization)",
        icon: "fa-search",
        desc: "Improve your Google ranking and get found by more customers. Comprehensive SEO strategies that drive organic traffic.",
        features: [
            "Google Ranking Improvement",
            "Keyword Optimization",
            "On-page & Off-page SEO",
            "Technical SEO Audit",
            "Content Optimization",
            "Link Building Strategies"
        ]
    },
    {
        title: "Digital Marketing",
        icon: "fa-bullhorn",
        desc: "Reach more customers with data-driven marketing campaigns. Measurable results across all digital channels.",
        features: [
            "Google Ads",
            "Meta Ads (Facebook & Instagram)",
            "Lead Generation Campaigns",
            "PPC Management",
            "Retargeting Campaigns",
            "Performance Tracking & Analytics"
        ]
    },
    {
        title: "Social Media Management",
        icon: "fa-hashtag",
        desc: "Grow your online presence with engaging content and strategic management across all social platforms.",
        features: [
            "Instagram Growth",
            "Content Creation (Posts, Reels)",
            "Page Handling & Strategy",
            "Community Management",
            "Influencer Collaboration",
            "Social Media Analytics"
        ]
    },
    {
        title: "Branding & Design",
        icon: "fa-paint-brush",
        desc: "Create a stunning brand identity that captivates your audience and stands out from the competition.",
        features: [
            "Logo Design",
            "Posters & Creatives",
            "UI/UX Design",
            "Brand Identity Development",
            "Visual Style Guides",
            "Marketing Material Design"
        ]
    },
    {
        title: "AI Automation",
        icon: "fa-robot",
        desc: "Transform your business with intelligent AI solutions that automate tasks, reduce costs, and boost productivity 24/7.",
        features: [
            "AI Chatbots (Website + WhatsApp Auto Reply)",
            "Lead Automation System (Auto Capture & Follow-up)",
            "Email & WhatsApp Marketing Automation",
            "CRM Automation (Customer Data Management)",
            "AI-based Customer Support (24/7 Response)",
            "Sales Funnel Automation",
            "AI Content Generation (Posts, Ads, Scripts)",
            "Workflow Automation (Business Process Auto)"
        ]
    }
];

const Services = () => {
    const [services, setServices] = useState([]);
    const [selectedService, setSelectedService] = useState(null);

    useEffect(() => {
        // Load services from localStorage (synced with admin panel)
        const storedServices = localStorage.getItem('services');
        
        // Check if stored services match our current default services structure
        let shouldUpdate = false;
        if (!storedServices) {
            shouldUpdate = true;
        } else {
            try {
                const parsed = JSON.parse(storedServices);
                // If number of services doesn't match or titles don't match, update
                if (parsed.length !== defaultServices.length) {
                    shouldUpdate = true;
                } else {
                    const titlesMatch = parsed.every((s, i) => s.title === defaultServices[i].title);
                    if (!titlesMatch) {
                        shouldUpdate = true;
                    }
                }
            } catch (e) {
                shouldUpdate = true;
            }
        }
        
        if (shouldUpdate || !storedServices) {
            setServices(defaultServices);
            localStorage.setItem('services', JSON.stringify(defaultServices));
        } else {
            setServices(JSON.parse(storedServices));
        }

        const isMobile = window.innerWidth <= 768;
        if (!isMobile) {
            const cards = document.querySelectorAll('.service-card');
            cards.forEach(card => {
                const handleMouseMove = (e) => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    card.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(59, 130, 246, 0.08), rgba(255, 255, 255, 0.03))`;
                };
                const handleMouseLeave = () => {
                    card.style.background = 'rgba(255, 255, 255, 0.03)';
                };
                card.addEventListener('mousemove', handleMouseMove);
                card.addEventListener('mouseleave', handleMouseLeave);
                return () => {
                    card.removeEventListener('mousemove', handleMouseMove);
                    card.removeEventListener('mouseleave', handleMouseLeave);
                };
            });
        }
    }, []);

    return (
        <section id="services" className="services">
            <div className="container">
                <h2 className="section-title">Our Professional Services</h2>
                <p className="section-subtitle">Complete digital solutions to grow your business online</p>

                <div className="marquee-background">
                    <div className="marquee-inner">
                        {[...Array(10)].map((_, i) => (
                            <span key={i}>SPECIAL OFFER • AADYAA INFOTECH • LIMITED PERIOD DEAL • </span>
                        ))}
                    </div>
                </div>

                <div className="services-grid">
                    {services.map((service, index) => (
                        <div className="service-card" key={index} onClick={() => setSelectedService(service)} style={{ cursor: 'pointer' }}>
                            <div className="icon-box">
                                <i className={`fas ${service.icon}`}></i>
                            </div>
                            <h3>{service.title}</h3>
                            <p>{service.desc}</p>
                            <ul className="service-features">
                                {service.features.map((feature, fIndex) => (
                                    <li key={fIndex}><i className="fas fa-check"></i> {feature}</li>
                                ))}
                            </ul>
                            {/* Internal links for SEO */}
                            {service.title === "Website Development" && (
                                <a href="#/services/website-development" className="learn-more-link" style={{ display: 'inline-block', marginTop: '1rem', color: '#3b82f6', textDecoration: 'none', fontWeight: '600' }}>
                                    Learn More About Website Development →
                                </a>
                            )}
                            {service.title === "Application Development" && (
                                <a href="#/services/application-development" className="learn-more-link" style={{ display: 'inline-block', marginTop: '1rem', color: '#3b82f6', textDecoration: 'none', fontWeight: '600' }}>
                                    Learn More About Application Development →
                                </a>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            {selectedService && (
                <div className="service-modal-overlay" onClick={() => setSelectedService(null)}>
                    <div className="service-modal-content" onClick={e => e.stopPropagation()}>
                        <button className="service-modal-close" onClick={() => setSelectedService(null)}>
                            <i className="fas fa-times"></i>
                        </button>
                        <div className="modal-icon-box">
                            <i className={`fas ${selectedService.icon}`}></i>
                        </div>
                        <h3>{selectedService.title}</h3>
                        <p>{selectedService.desc}</p>
                        <ul className="modal-features">
                            {selectedService.features.map((feature, idx) => (
                                <li key={idx}><i className="fas fa-check"></i> {feature}</li>
                            ))}
                        </ul>
                        <div style={{ marginTop: '2rem', textAlign: 'center' }}>
                            <button className="btn-primary-soft" onClick={() => {
                                const text = `Thank you for contacting Aadyaa Infotech. We truly appreciate your message. Our team will review your inquiry and get back to you shortly.\n\nInquiry about: ${selectedService.title}`;
                                window.location.href = `https://wa.me/916355893624?text=${encodeURIComponent(text)}`;
                            }}>
                                Inquiry Now <i className="fab fa-whatsapp" style={{ marginLeft: '8px' }}></i>
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </section>
    );
};

export default Services;
