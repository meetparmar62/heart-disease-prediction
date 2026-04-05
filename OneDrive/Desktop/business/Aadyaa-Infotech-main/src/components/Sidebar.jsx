import React from 'react';

const Sidebar = ({ isOpen, onClose }) => {
    return (
        <>
            <div
                className={`sidebar-overlay ${isOpen ? 'active' : ''}`}
                id="sidebarOverlay"
                onClick={onClose}
            ></div>
            <div className={`sidebar-menu ${isOpen ? 'active' : ''}`} id="sidebarMenu">
                <div className="sidebar-header">
                    <div className="sidebar-logo">
                        <h2><span className="gradient-text">Aadyaa</span> Infotech</h2>
                    </div>
                    <button className="sidebar-close" id="sidebarClose" onClick={onClose}>
                        <i className="fas fa-times"></i>
                    </button>
                </div>
                <div className="sidebar-content">
                    <ul className="sidebar-nav">
                        <li className="sidebar-item">
                            <a href="#contact" className="sidebar-link" onClick={onClose}>
                                <span className="link-icon"><i className="fas fa-envelope"></i></span>
                                <span className="link-text">Contact Us</span>
                                <span className="link-arrow"><i className="fas fa-chevron-right"></i></span>
                            </a>
                        </li>
                        <li className="sidebar-item">
                            <a href="#services" className="sidebar-link" onClick={onClose}>
                                <span className="link-icon"><i className="fas fa-layer-group"></i></span>
                                <span className="link-text">Services</span>
                                <span className="link-arrow"><i className="fas fa-chevron-right"></i></span>
                            </a>
                        </li>
                    </ul>
                </div>
                <div className="sidebar-footer">
                    <div className="sidebar-social">
                        <a href="https://www.facebook.com/share/1AhUFCfrv7/" target="_blank" rel="noopener noreferrer" className="social-icon"><i className="fab fa-facebook"></i></a>
                        <a href="https://www.linkedin.com/company/aadyaa-infotech" target="_blank" rel="noopener noreferrer" className="social-icon"><i className="fab fa-linkedin"></i></a>
                        <a href="https://www.instagram.com/aadyaa_infotech" target="_blank" rel="noopener noreferrer" className="social-icon"><i className="fab fa-instagram"></i></a>
                        <a href="https://wa.me/916355893624" target="_blank" rel="noopener noreferrer" className="social-icon"><i className="fab fa-whatsapp"></i></a>
                    </div>
                    <p className="copyright">© 2024 Aadyaa Infotech</p>
                </div>
            </div>
        </>
    );
};

export default Sidebar;
