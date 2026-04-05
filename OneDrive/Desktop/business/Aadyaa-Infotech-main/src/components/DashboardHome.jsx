import React from 'react';

const DashboardHome = ({ services, inquiries }) => {
  // Load all data from localStorage for complete stats
  const teamMembers = JSON.parse(localStorage.getItem('teamMembers') || '[]');
  const projects = JSON.parse(localStorage.getItem('projects') || '[]');
  const testimonials = JSON.parse(localStorage.getItem('testimonials') || '[]');
  
  const totalServices = services.length;
  const totalInquiries = inquiries.length;
  const newInquiries = inquiries.filter(i => i.status === 'new').length;
  const contactedInquiries = inquiries.filter(i => i.status === 'contacted').length;
  const closedInquiries = inquiries.filter(i => i.status === 'closed').length;

  const recentInquiries = inquiries.slice(-5).reverse();

  return (
    <div className="dashboard-home">
      <div className="admin-header">
        <h1>Dashboard Overview</h1>
        <p>Welcome to Aadyaa Infotech Admin Panel</p>
      </div>

      <div className="stats-grid">
        <div className="stat-card-admin">
          <div className="stat-icon" style={{ background: 'linear-gradient(135deg, #6366f1, #8b5cf6)' }}>
            <i className="fas fa-briefcase"></i>
          </div>
          <div className="stat-info">
            <h3>{totalServices}</h3>
            <p>Total Services</p>
          </div>
        </div>

        <div className="stat-card-admin">
          <div className="stat-icon" style={{ background: 'linear-gradient(135deg, #ec4899, #f59e0b)' }}>
            <i className="fas fa-users"></i>
          </div>
          <div className="stat-info">
            <h3>{teamMembers.length || 3}</h3>
            <p>Team Members</p>
          </div>
        </div>

        <div className="stat-card-admin">
          <div className="stat-icon" style={{ background: 'linear-gradient(135deg, #10b981, #3b82f6)' }}>
            <i className="fas fa-folder-open"></i>
          </div>
          <div className="stat-info">
            <h3>{projects.length}</h3>
            <p>Projects Done</p>
          </div>
        </div>

        <div className="stat-card-admin">
          <div className="stat-icon" style={{ background: 'linear-gradient(135deg, #3b82f6, #6366f1)' }}>
            <i className="fas fa-comments"></i>
          </div>
          <div className="stat-info">
            <h3>{testimonials.length}</h3>
            <p>Testimonials</p>
          </div>
        </div>

        <div className="stat-card-admin">
          <div className="stat-icon" style={{ background: 'linear-gradient(135deg, #f59e0b, #ef4444)' }}>
            <i className="fas fa-envelope"></i>
          </div>
          <div className="stat-info">
            <h3>{totalInquiries}</h3>
            <p>Total Inquiries</p>
          </div>
        </div>

        <div className="stat-card-admin">
          <div className="stat-icon" style={{ background: 'linear-gradient(135deg, #10b981, #3b82f6)' }}>
            <i className="fas fa-clock"></i>
          </div>
          <div className="stat-info">
            <h3>{newInquiries}</h3>
            <p>New Inquiries</p>
          </div>
        </div>

        <div className="stat-card-admin">
          <div className="stat-icon" style={{ background: 'linear-gradient(135deg, #3b82f6, #8b5cf6)' }}>
            <i className="fas fa-phone-alt"></i>
          </div>
          <div className="stat-info">
            <h3>{contactedInquiries}</h3>
            <p>Contacted</p>
          </div>
        </div>

        <div className="stat-card-admin">
          <div className="stat-icon" style={{ background: 'linear-gradient(135deg, #6b7280, #9ca3af)' }}>
            <i className="fas fa-check-circle"></i>
          </div>
          <div className="stat-info">
            <h3>{closedInquiries}</h3>
            <p>Closed/Converted</p>
          </div>
        </div>
      </div>

      <div className="recent-activity">
        <h2>Recent Inquiries</h2>
        <div className="activity-list">
          {recentInquiries.length > 0 ? (
            recentInquiries.map(inquiry => (
              <div key={inquiry.id} className="activity-item">
                <div className="activity-icon">
                  <i className={`fas ${inquiry.service.includes('Website') ? 'fa-laptop-code' : 'fa-shopping-cart'}`}></i>
                </div>
                <div className="activity-details">
                  <h4>{inquiry.name}</h4>
                  <p>{inquiry.service}</p>
                  <span className="activity-date">{new Date(inquiry.date).toLocaleDateString()}</span>
                </div>
                <div className={`status-badge ${inquiry.status}`}>
                  {inquiry.status}
                </div>
              </div>
            ))
          ) : (
            <p className="no-data">No inquiries yet</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default DashboardHome;
