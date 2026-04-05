import React from 'react';

const DemoSites = () => {
    return (
        <section id="demo-sites" className="demo-sites-section">
            <div className="container">
                <h2 className="section-title">Our New Demo Dynamic Web or App</h2>
                <p className="section-subtitle">Explore our latest interactive projects and applications</p>
                <div className="demo-grid">
                    <div className="demo-card">
                        <div className="demo-image-wrapper">
                            <img src="/1.png" alt="E-commerce Dynamics" className="demo-img" />
                        </div>
                        <div className="demo-content">
                          <h3>E-commerce Dynamics</h3>
                            <p>A fully functional dynamic web app for e-commerce with real-time updates.</p>
                            <button className="btn-primary-soft" onClick={() => {
                                const text = `Thank you for contacting Aadyaa Infotech. We truly appreciate your message. Our team will review your inquiry and get back to you shortly.\n\nInquiry about: E-commerce Dynamics`;
                                window.location.href = `https://wa.me/916355893624?text=${encodeURIComponent(text)}`;
                            }}>Inquiry Now <i className="fab fa-whatsapp"></i></button>
                        </div>
                    </div>
                    <div className="demo-card">
                        <div className="demo-image-wrapper">
                            <img src="/2.png" alt="Healthcare Dashboard" className="demo-img" />
                        </div>
                        <div className="demo-content">
                            <h3>Healthcare Dashboard</h3>
                            <p>Modern and responsive demo of a dashboard tailored for healthcare facilities.</p>
                            <button className="btn-primary-soft" onClick={() => {
                                const text = `Thank you for contacting Aadyaa Infotech. We truly appreciate your message. Our team will review your inquiry and get back to you shortly.\n\nInquiry about: Healthcare Dashboard`;
                                window.location.href = `https://wa.me/916355893624?text=${encodeURIComponent(text)}`;
                            }}>Inquiry Now <i className="fab fa-whatsapp"></i></button>
                        </div>
                    </div>
                    <div className="demo-card">
                        <div className="demo-image-wrapper">
                            <img src="/3.png" alt="Portfolio Agency" className="demo-img" />
                        </div>
                        <div className="demo-content">
                            <h3>Portfolio Agency</h3>
                            <p>An interactive portfolio template featuring rich animations and smooth transitions.</p>
                            <button className="btn-primary-soft" onClick={() => {
                                const text = `Thank you for contacting Aadyaa Infotech. We truly appreciate your message. Our team will review your inquiry and get back to you shortly.\n\nInquiry about: Portfolio Agency`;
                                window.location.href = `https://wa.me/916355893624?text=${encodeURIComponent(text)}`;
                            }}>Inquiry Now <i className="fab fa-whatsapp"></i></button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default DemoSites;
