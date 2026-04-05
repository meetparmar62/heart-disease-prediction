import React from 'react';

const AdminSidebar = ({ activeSection, onSectionChange, onLogout, user }) => {
  const menuItems = [
    { id: 'dashboard', label: 'Dashboard', icon: 'fa-home' },
    { id: 'services', label: 'Services', icon: 'fa-briefcase' },
    { id: 'projects', label: 'Projects', icon: 'fa-folder-open' },
    { id: 'team', label: 'Team', icon: 'fa-users' },
    { id: 'testimonials', label: 'Testimonials', icon: 'fa-comments' },
    { id: 'inquiries', label: 'Inquiries', icon: 'fa-envelope' },
    { id: 'analytics', label: 'Analytics', icon: 'fa-chart-line' },
    { id: 'settings', label: 'Settings', icon: 'fa-cog' }
  ];

  return (
    <div className="admin-sidebar">
      <div className="sidebar-header">
        <img src="/logo.png" alt="Logo" className="sidebar-logo" />
        <h3>Aadyaa Admin</h3>
        <p>Welcome, {user}</p>
      </div>

      <nav className="sidebar-nav">
        {menuItems.map(item => (
          <button
            key={item.id}
            className={`nav-item ${activeSection === item.id ? 'active' : ''}`}
            onClick={() => onSectionChange(item.id)}
          >
            <i className={`fas ${item.icon}`}></i>
            <span>{item.label}</span>
          </button>
        ))}
      </nav>

      <button className="nav-item logout-btn" onClick={onLogout}>
        <i className="fas fa-sign-out-alt"></i>
        <span>Logout</span>
      </button>
    </div>
  );
};

export default AdminSidebar;
