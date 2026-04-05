import React, { useState } from 'react';
import AdminLogin from './AdminLogin';
import AdminDashboard from './AdminDashboard';

const AdminPanel = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [adminUser, setAdminUser] = useState(null);

  const handleLogin = (username) => {
    setIsAuthenticated(true);
    setAdminUser(username);
    localStorage.setItem('adminAuthenticated', 'true');
    localStorage.setItem('adminUser', username);
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    setAdminUser(null);
    localStorage.removeItem('adminAuthenticated');
    localStorage.removeItem('adminUser');
  };

  return (
    <div className="admin-panel-wrapper">
      {!isAuthenticated ? (
        <AdminLogin onLogin={handleLogin} />
      ) : (
        <AdminDashboard user={adminUser} onLogout={handleLogout} />
      )}
    </div>
  );
};

export default AdminPanel;
