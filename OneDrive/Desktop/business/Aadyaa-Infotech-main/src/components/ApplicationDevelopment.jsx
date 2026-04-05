import React from 'react';
import { Helmet } from 'react-helmet-async';

const ApplicationDevelopment = () => {
  return (
    <>
      <Helmet>
        <title>Application Development Company in Ahmedabad | Mobile App Developers - Aadyaa Infotech</title>
        <meta name="description" content="Professional application development company in Ahmedabad offering Android app development, iOS app development, cross-platform apps & custom mobile solutions. Get free quote!" />
        <meta name="keywords" content="application development Ahmedabad, mobile app development Ahmedabad, Android app developer Ahmedabad, iOS app developer Ahmedabad, cross-platform app development, React Native developers Gujarat, custom mobile apps, app development company" />
        <link rel="canonical" href="https://aadyaainfotech.in/#/services/application-development" />
      </Helmet>

      <section className="service-detail-page" style={{ padding: '100px 20px', maxWidth: '1200px', margin: '0 auto' }}>
        <div className="container">
          {/* Breadcrumb Navigation */}
          <nav style={{ marginBottom: '2rem', fontSize: '0.9rem' }}>
            <a href="#/" style={{ color: '#3b82f6', textDecoration: 'none' }}>Home</a>
            <span style={{ margin: '0 0.5rem', color: '#6b7280' }}>/</span>
            <a href="#services" style={{ color: '#3b82f6', textDecoration: 'none' }}>Services</a>
            <span style={{ margin: '0 0.5rem', color: '#6b7280' }}>/</span>
            <span style={{ color: '#6b7280' }}>Application Development</span>
          </nav>

          <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: '#3b82f6' }}>
            Professional Application Development Services in Ahmedabad
          </h1>
          
          <p style={{ fontSize: '1.2rem', marginBottom: '2rem', lineHeight: '1.8' }}>
            Aadyaa Infotech is a leading application development company in Ahmedabad, specializing in creating innovative mobile applications for Android and iOS platforms. We deliver high-quality, user-friendly apps that help businesses engage customers and drive growth. Serving businesses across SG Highway, Satellite, Vastrapur, Bodakdev, Prahlad Nagar, Thaltej, Navrangpura, Maninagar, Nikol, Bopal, and all areas in Ahmedabad.
          </p>

          {/* Service Areas Section */}
          <div style={{ marginTop: '2rem', padding: '2rem', background: 'linear-gradient(135deg, rgba(59, 130, 246, 0.05), rgba(147, 51, 234, 0.05))', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
            <h3 style={{ color: '#3b82f6', marginBottom: '1rem', fontSize: '1.5rem' }}>
              <i className="fas fa-map-marker-alt" style={{ marginRight: '0.5rem' }}></i>
              Application Development Services Across Ahmedabad
            </h3>
            <p style={{ marginBottom: '1rem' }}>We provide professional mobile app development services throughout Ahmedabad and surrounding areas:</p>
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
              <h3 style={{ color: '#3b82f6', marginBottom: '1rem' }}>Android App Development</h3>
              <p>Custom Android applications built with native technologies for optimal performance and user experience on all Android devices.</p>
              <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
                <li>Native Android Apps (Kotlin/Java)</li>
                <li>Material Design UI/UX</li>
                <li>Google Play Store Publishing</li>
                <li>Performance Optimization</li>
              </ul>
            </div>

            <div style={{ padding: '2rem', background: 'rgba(59, 130, 246, 0.05)', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
              <h3 style={{ color: '#3b82f6', marginBottom: '1rem' }}>iOS App Development</h3>
              <p>Premium iOS applications designed specifically for iPhone and iPad users with seamless integration into the Apple ecosystem.</p>
              <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
                <li>Native iOS Apps (Swift)</li>
                <li>Apple Design Guidelines</li>
                <li>App Store Submission</li>
                <li>iCloud Integration</li>
              </ul>
            </div>

            <div style={{ padding: '2rem', background: 'rgba(59, 130, 246, 0.05)', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
              <h3 style={{ color: '#3b82f6', marginBottom: '1rem' }}>Cross-Platform Development</h3>
              <p>Cost-effective cross-platform applications that work seamlessly on both Android and iOS using modern frameworks.</p>
              <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
                <li>React Native Development</li>
                <li>Flutter Development</li>
                <li>Single Codebase</li>
                <li>Faster Time to Market</li>
              </ul>
            </div>

            <div style={{ padding: '2rem', background: 'rgba(59, 130, 246, 0.05)', borderRadius: '10px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
              <h3 style={{ color: '#3b82f6', marginBottom: '1rem' }}>Custom Business Apps</h3>
              <p>Tailored mobile solutions designed to streamline your business operations and improve productivity.</p>
              <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
                <li>Enterprise Applications</li>
                <li>E-commerce Apps</li>
                <li>Booking & Reservation Apps</li>
                <li>Social Networking Apps</li>
              </ul>
            </div>
          </div>

          <div style={{ marginTop: '4rem', textAlign: 'center' }}>
            <h2 style={{ fontSize: '2rem', marginBottom: '1.5rem' }}>Our Application Development Process</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '2rem', marginTop: '2rem' }}>
              <div>
                <div style={{ width: '60px', height: '60px', borderRadius: '50%', background: '#3b82f6', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem', fontWeight: 'bold', margin: '0 auto 1rem' }}>1</div>
                <h4>Discovery & Planning</h4>
                <p>Understanding your requirements and defining project scope</p>
              </div>
              <div>
                <div style={{ width: '60px', height: '60px', borderRadius: '50%', background: '#3b82f6', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem', fontWeight: 'bold', margin: '0 auto 1rem' }}>2</div>
                <h4>UI/UX Design</h4>
                <p>Creating intuitive and visually appealing app designs</p>
              </div>
              <div>
                <div style={{ width: '60px', height: '60px', borderRadius: '50%', background: '#3b82f6', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem', fontWeight: 'bold', margin: '0 auto 1rem' }}>3</div>
                <h4>Development</h4>
                <p>Building your app with clean, scalable code</p>
              </div>
              <div>
                <div style={{ width: '60px', height: '60px', borderRadius: '50%', background: '#3b82f6', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem', fontWeight: 'bold', margin: '0 auto 1rem' }}>4</div>
                <h4>Testing & Launch</h4>
                <p>Rigorous testing and successful app store deployment</p>
              </div>
            </div>
          </div>

          <div style={{ marginTop: '4rem', textAlign: 'center' }}>
            <h2 style={{ fontSize: '2rem', marginBottom: '1.5rem' }}>Why Choose Aadyaa Infotech for App Development in Ahmedabad?</h2>
            <p style={{ fontSize: '1.1rem', marginBottom: '2rem', maxWidth: '800px', margin: '0 auto 2rem', lineHeight: '1.8' }}>
              As a leading application development company in Ahmedabad, we've successfully delivered mobile apps for businesses across SG Highway, Satellite, Vastrapur, Bodakdev, and all areas of Ahmedabad. Our local expertise combined with technical excellence makes us the preferred choice for app development in Ahmedabad.
            </p>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '2rem', marginTop: '2rem' }}>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Local Ahmedabad Expertise</h4>
                <p>We understand the Ahmedabad market and create apps that resonate with local users</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Experienced Developers</h4>
                <p>Skilled team with expertise in latest mobile technologies</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>User-Centric Design</h4>
                <p>Apps designed with focus on user experience and engagement</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Quality Assurance</h4>
                <p>Thorough testing to ensure bug-free, reliable applications</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Post-Launch Support</h4>
                <p>Ongoing maintenance and updates to keep your app running smoothly</p>
              </div>
              <div>
                <i className="fas fa-check-circle" style={{ fontSize: '2rem', color: '#10b981', marginBottom: '1rem' }}></i>
                <h4>Affordable Pricing</h4>
                <p>Competitive pricing for businesses in Ahmedabad without compromising quality</p>
              </div>
            </div>
          </div>

          <div style={{ marginTop: '4rem', textAlign: 'center', padding: '3rem', background: 'linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 51, 234, 0.1))', borderRadius: '15px' }}>
            <h2 style={{ fontSize: '2rem', marginBottom: '1rem' }}>Ready to Build Your Mobile App?</h2>
            <p style={{ fontSize: '1.2rem', marginBottom: '2rem' }}>Get a free consultation and quote for your application development project</p>
            <a 
              href="https://wa.me/916355893624?text=Hi, I'm interested in application development services" 
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
              <a href="#/services/website-development" style={{ color: '#3b82f6', textDecoration: 'none', padding: '0.75rem 1.5rem', border: '1px solid #3b82f6', borderRadius: '8px', transition: 'all 0.3s' }}>
                <i className="fas fa-laptop-code" style={{ marginRight: '0.5rem' }}></i>
                Website Development
              </a>
              <a href="#services" style={{ color: '#3b82f6', textDecoration: 'none', padding: '0.75rem 1.5rem', border: '1px solid #3b82f6', borderRadius: '8px', transition: 'all 0.3s' }}>
                <i className="fas fa-paint-brush" style={{ marginRight: '0.5rem' }}></i>
                UI/UX Design
              </a>
              <a href="#services" style={{ color: '#3b82f6', textDecoration: 'none', padding: '0.75rem 1.5rem', border: '1px solid #3b82f6', borderRadius: '8px', transition: 'all 0.3s' }}>
                <i className="fas fa-robot" style={{ marginRight: '0.5rem' }}></i>
                AI Automation
              </a>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default ApplicationDevelopment;
