import React from 'react';
import { Helmet } from 'react-helmet-async';

const WebsiteDevelopment = () => {
  return (
    <>
      <Helmet>
        <title>Website Development Company in Ahmedabad | Custom Web Design Services - Aadyaa Infotech</title>
        <meta name="description" content="Professional website development company in Ahmedabad offering custom web design, e-commerce websites, responsive web development & SEO-friendly sites. Get free consultation!" />
        <meta name="keywords" content="website development Ahmedabad, web design Ahmedabad, custom website development, e-commerce website Ahmedabad, responsive web design, WordPress development Ahmedabad, business website developer, professional web development Gujarat" />
        <link rel="canonical" href="https://aadyaainfotech.in/#/services/website-development" />
      </Helmet>

      <section className="service-detail-page" style={{ padding: '100px 20px', maxWidth: '1200px', margin: '0 auto' }}>
        <div className="container">
          {/* Breadcrumb Navigation */}
          <nav style={{ marginBottom: '2rem', fontSize: '0.9rem' }}>
            <a href="#/" style={{ color: '#3b82f6', textDecoration: 'none' }}>Home</a>
            <span style={{ margin: '0 0.5rem', color: '#6b7280' }}>/</span>
            <a href="#services" style={{ color: '#3b82f6', textDecoration: 'none' }}>Services</a>
            <span style={{ margin: '0 0.5rem', color: '#6b7280' }}>/</span>
            <span style={{ color: '#6b7280' }}>Website Development</span>
          </nav>

          <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: '#3b82f6' }}>
            Professional Website Development Services in Ahmedabad
          </h1>
          
          <p style={{ fontSize: '1.2rem', marginBottom: '2rem', lineHeight: '1.8' }}>
            Aadyaa Infotech is a leading website development company in Ahmedabad, Gujarat. We specialize in creating custom, responsive, and SEO-friendly websites that help businesses grow their online presence and convert visitors into customers. Serving clients across all areas of Ahmedabad including SG Highway, Satellite, Vastrapur, Bodakdev, Prahlad Nagar, Thaltej, Navrangpura, Maninagar, Nikol, Bopal, and more.
          </p>

          {/* Service Areas Section */}
          <div style={{ marginTop: '2rem', padding: '2rem', background: 'linear-gradient(135deg, rgba(59, 130, 246, 0.05), rgba(147, 51, 234, 0.05))', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
            <h3 style={{ color: '#3b82f6', marginBottom: '1rem', fontSize: '1.5rem' }}>
              <i className="fas fa-map-marker-alt" style={{ marginRight: '0.5rem' }}></i>
              Website Development Services Across Ahmedabad
            </h3>
            <p style={{ marginBottom: '1rem' }}>We provide professional website development services throughout Ahmedabad and surrounding areas:</p>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>SG Highway</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Satellite</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Vastrapur</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Bodakdev</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Prahlad Nagar</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Thaltej</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Navrangpura</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Maninagar</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Nikol</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Bopal</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Ambli</div>
              <div><i className="fas fa-check" style={{ color: '#10b981', marginRight: '0.5rem' }}></i>Gota</div>
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem', marginTop: '3rem' }}>
            <div style={{ padding: '2rem', background: 'rgba(59, 130, 246, 0.05)', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
              <h3 style={{ color: '#3b82f6', marginBottom: '1rem' }}>Custom Website Development</h3>
              <p>Tailor-made websites designed specifically for your business needs. From simple landing pages to complex web applications, we build solutions that scale with your business.</p>
              <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
                <li>Business Websites</li>
                <li>Corporate Portals</li>
                <li>Landing Pages</li>
                <li>Web Applications</li>
              </ul>
            </div>

            <div style={{ padding: '2rem', background: 'rgba(59, 130, 246, 0.05)', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
              <h3 style={{ color: '#3b82f6', marginBottom: '1rem' }}>E-commerce Website Development</h3>
              <p>Complete e-commerce solutions with secure payment gateways, inventory management, and user-friendly interfaces to maximize your online sales.</p>
              <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
                <li>Online Stores</li>
                <li>Shopping Carts</li>
                <li>Payment Integration</li>
                <li>Product Management</li>
              </ul>
            </div>

            <div style={{ padding: '2rem', background: 'rgba(59, 130, 246, 0.05)', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
              <h3 style={{ color: '#3b82f6', marginBottom: '1rem' }}>Responsive Web Design</h3>
              <p>Mobile-first websites that look stunning on all devices. Our responsive designs ensure your website provides an excellent user experience on desktops, tablets, and smartphones.</p>
              <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
                <li>Mobile-First Approach</li>
                <li>Cross-Browser Compatibility</li>
                <li>Fast Loading Speed</li>
                <li>Touch-Friendly Interfaces</li>
              </ul>
            </div>

            <div style={{ padding: '2rem', background: 'rgba(59, 130, 246, 0.05)', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
              <h3 style={{ color: '#3b82f6', marginBottom: '1rem' }}>WordPress Development</h3>
              <p>Custom WordPress themes and plugins development. We create easy-to-manage websites with powerful content management systems.</p>
              <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
                <li>Custom Themes</li>
                <li>Plugin Development</li>
                <li>WooCommerce Stores</li>
                <li>WordPress Maintenance</li>
              </ul>
            </div>
          </div>

          <div style={{ marginTop: '4rem', textAlign: 'center' }}>
            <h2 style={{ fontSize: '2rem', marginBottom: '1.5rem' }}>Why Choose Aadyaa Infotech for Website Development in Ahmedabad?</h2>
            <p style={{ fontSize: '1.1rem', marginBottom: '2rem', maxWidth: '800px', margin: '0 auto 2rem', lineHeight: '1.8' }}>
              As a trusted website development company in Ahmedabad, we understand the local market and business needs. From startups in SG Highway to established businesses in Satellite and Vastrapur, we've helped hundreds of clients across Ahmedabad establish their digital presence.
            </p>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '2rem', marginTop: '2rem' }}>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Local Ahmedabad Expertise</h4>
                <p>We understand the Ahmedabad market and create websites that resonate with local customers</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>SEO-Friendly Architecture</h4>
                <p>Websites built with clean code and proper structure for better search engine rankings</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Fast Performance</h4>
                <p>Optimized websites that load quickly and provide smooth user experience</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Secure & Reliable</h4>
                <p>Implementation of security best practices to protect your website and data</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>24/7 Support</h4>
                <p>Dedicated support team available to help you with any issues or updates</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Affordable Pricing</h4>
                <p>Competitive pricing for businesses in Ahmedabad without compromising quality</p>
              </div>
            </div>
          </div>

          <div style={{ marginTop: '4rem', textAlign: 'center', padding: '3rem', background: 'linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 51, 234, 0.1))', borderRadius: '15px' }}>
            <h2 style={{ fontSize: '2rem', marginBottom: '1rem' }}>Ready to Build Your Website?</h2>
            <p style={{ fontSize: '1.2rem', marginBottom: '2rem' }}>Get a free consultation and quote for your website development project</p>
            <a 
              href="https://wa.me/916355893624?text=Hi, I'm interested in website development services" 
              className="btn-primary-soft"
              style={{ display: 'inline-block', padding: '1rem 2rem', textDecoration: 'none' }}
            >
              <i className="fab fa-whatsapp" style={{ marginRight: '8px' }}></i>
              Contact Us Now
            </a>
          </div>

          {/* Related Services */}
          <div style={{ marginTop: '4rem', paddingTop: '3rem', borderTop: '1px solid rgba(59, 130, 246, 0.2)' }}>
            <h3 style={{ fontSize: '1.5rem', marginBottom: '1.5rem', textAlign: 'center' }}>Related Services</h3>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '2rem', flexWrap: 'wrap' }}>
              <a href="#/services/application-development" style={{ color: '#3b82f6', textDecoration: 'none', padding: '0.75rem 1.5rem', border: '1px solid #3b82f6', borderRadius: '8px', transition: 'all 0.3s' }}>
                <i className="fas fa-mobile-alt" style={{ marginRight: '0.5rem' }}></i>
                Application Development
              </a>
              <a href="#services" style={{ color: '#3b82f6', textDecoration: 'none', padding: '0.75rem 1.5rem', border: '1px solid #3b82f6', borderRadius: '8px', transition: 'all 0.3s' }}>
                <i className="fas fa-search" style={{ marginRight: '0.5rem' }}></i>
                SEO Services
              </a>
              <a href="#services" style={{ color: '#3b82f6', textDecoration: 'none', padding: '0.75rem 1.5rem', border: '1px solid #3b82f6', borderRadius: '8px', transition: 'all 0.3s' }}>
                <i className="fas fa-bullhorn" style={{ marginRight: '0.5rem' }}></i>
                Digital Marketing
              </a>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default WebsiteDevelopment;
