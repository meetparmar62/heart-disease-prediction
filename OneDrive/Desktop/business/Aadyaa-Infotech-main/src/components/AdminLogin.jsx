import React, { useState } from 'react';

const AdminLogin = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Simple authentication (you can enhance this later)
    if (username === 'admin' && password === 'admin123') {
      onLogin(username);
      setError('');
    } else {
      setError('Invalid username or password');
    }
  };

  return (
    <div className="admin-login-container">
      <div className="admin-login-card">
        <div className="login-header">
          <img src="/logo.png" alt="Aadyaa Infotech" className="login-logo" />
          <h1>Admin Panel</h1>
          <p>Sign in to manage your website</p>
        </div>

        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter username"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password"
              required
            />
          </div>

          {error && <div className="error-message">{error}</div>}

          <button type="submit" className="btn-admin-login">
            Sign In
          </button>

          {/* <div className="login-hint">
            <p>Default credentials:</p>
            <code>Username: admin | Password: admin123</code>
          </div> */}
        </form>
      </div>
    </div>
  );
};

export default AdminLogin;
