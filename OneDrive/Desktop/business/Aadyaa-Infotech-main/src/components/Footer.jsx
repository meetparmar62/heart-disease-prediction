import React from 'react';

const Footer = () => {
    const currentYear = new Date().getFullYear();

    return (
        <>
            <footer className="footer">
                <div className="container footer-container">
                    <div className="footer-content">
                        {/* Company Info Section */}
                        <div className="footer-section footer-about">
                            <h3>Aadyaa Infotech</h3>
                            <p className="footer-description">
                                Empowering businesses through innovative digital solutions. 
                                Your trusted partner for digital transformation and sustainable growth.
                            </p>
                            <div className="footer-social-links">
                                <a href="https://linkedin.com/company/aadyaa-infotech" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                                    <i className="fab fa-linkedin-in"></i>
                                </a>
                                <a href="https://github.com/aadyaainfotech" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
                                    <i className="fab fa-github"></i>
                                </a>
                                <a href="https://twitter.com/aadyaainfotech" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
                                    <i className="fab fa-twitter"></i>
                                </a>
                                <a href="https://facebook.com/aadyaainfotech" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
                                    <i className="fab fa-facebook-f"></i>
                                </a>
                            </div>
                        </div>

                        {/* Quick Links Section */}
                        <div className="footer-section">
                            <h4>Quick Links</h4>
                            <ul>
                                <li><a href="#home"><i className="fas fa-angle-right"></i> Home</a></li>
                                <li><a href="#about"><i className="fas fa-angle-right"></i> About Us</a></li>
                                <li><a href="#services"><i className="fas fa-angle-right"></i> Services</a></li>
                                <li><a href="#projects"><i className="fas fa-angle-right"></i> Projects</a></li>
                                <li><a href="#team"><i className="fas fa-angle-right"></i> Team</a></li>
                                <li><a href="#contact"><i className="fas fa-angle-right"></i> Contact</a></li>
                            </ul>
                        </div>

                        {/* Services Section */}
                        <div className="footer-section">
                            <h4>Our Services</h4>
                            <ul>
                                <li><a href="#services"><i className="fas fa-angle-right"></i> Website Development</a></li>
                                <li><a href="#services"><i className="fas fa-angle-right"></i> Mobile App Development</a></li>
                                <li><a href="#services"><i className="fas fa-angle-right"></i> UI/UX Design</a></li>
                                <li><a href="#services"><i className="fas fa-angle-right"></i> SEO & Digital Marketing</a></li>
                                <li><a href="#services"><i className="fas fa-angle-right"></i> Graphic Design</a></li>
                                <li><a href="#services"><i className="fas fa-angle-right"></i> E-commerce Solutions</a></li>
                                <li><a href="#services"><i className="fas fa-angle-right"></i> Business Consulting</a></li>
                            </ul>
                        </div>

                        {/* Industries Section */}
                        <div className="footer-section">
                            <h4>Industries</h4>
                            <ul>
                                <li><a href="#industries"><i className="fas fa-angle-right"></i> Healthcare</a></li>
                                <li><a href="#industries"><i className="fas fa-angle-right"></i> E-commerce & Retail</a></li>
                                <li><a href="#industries"><i className="fas fa-angle-right"></i> Education</a></li>
                                <li><a href="#industries"><i className="fas fa-angle-right"></i> Finance</a></li>
                                <li><a href="#industries"><i className="fas fa-angle-right"></i> Real Estate</a></li>
                                <li><a href="#industries"><i className="fas fa-angle-right"></i> Manufacturing</a></li>
                            </ul>
                        </div>
                    </div>

                    {/* Footer Bottom */}
                    <div className="footer-bottom">
                        <div className="footer-bottom-content">
                            <p>&copy; {currentYear} Aadyaa Infotech. All Rights Reserved.</p>
                            <div className="footer-bottom-links">
                                <a href="#privacy">Privacy Policy</a>
                                <a href="#terms">Terms of Service</a>
                                <a href="#cookies">Cookie Policy</a>
                            </div>
                            <p className="footer-tagline">Designed with <i className="fas fa-heart"></i> by Aadyaa Infotech</p>
                        </div>
                    </div>
                </div>
            </footer>

            <button className="scroll-top" id="scrollTop" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>
                <i className="fas fa-arrow-up"></i>
            </button>
        </>
    );
};

export default Footer;
