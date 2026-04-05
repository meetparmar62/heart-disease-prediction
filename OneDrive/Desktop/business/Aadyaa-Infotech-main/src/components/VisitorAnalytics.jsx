import React, { useState, useEffect } from 'react';
import { getVisitorCount } from '../utils/visitorTracking';

const VisitorAnalytics = () => {
  const [visitorCount, setVisitorCount] = useState(0);
  const [visitorLogs, setVisitorLogs] = useState([]);
  const [conversions, setConversions] = useState([]);
  const [selectedTab, setSelectedTab] = useState('overview');

  useEffect(() => {
    loadAnalytics();
  }, []);

  const loadAnalytics = async () => {
    // Load visitor count
    const count = await getVisitorCount();
    setVisitorCount(count || 0);

    // Load visitor logs from localStorage
    const logs = JSON.parse(localStorage.getItem('visitorLogs') || '[]');
    setVisitorLogs(logs.reverse()); // Show newest first

    // Load conversions
    const conv = JSON.parse(localStorage.getItem('conversions') || '[]');
    setConversions(conv.reverse());
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString('en-IN', {
      day: '2-digit',
      month: 'short',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getBrowserIcon = (userAgent) => {
    if (userAgent.includes('Chrome')) return 'fa-chrome';
    if (userAgent.includes('Firefox')) return 'fa-firefox';
    if (userAgent.includes('Safari')) return 'fa-safari';
    if (userAgent.includes('Edge')) return 'fa-edge';
    return 'fa-globe';
  };

  const getDeviceIcon = (userAgent) => {
    if (userAgent.includes('Mobile')) return 'fa-mobile-alt';
    if (userAgent.includes('Tablet')) return 'fa-tablet';
    return 'fa-desktop';
  };

  const getTotalConversions = () => {
    return conversions.length;
  };

  const getServiceBreakdown = () => {
    const breakdown = {};
    conversions.forEach(conv => {
      const service = conv.data?.service || 'Unknown';
      breakdown[service] = (breakdown[service] || 0) + 1;
    });
    return breakdown;
  };

  return (
    <div className="visitor-analytics">
      <div className="admin-header">
        <h1>
          <i className="fas fa-chart-line"></i> Visitor Analytics
        </h1>
      </div>

      {/* Stats Cards */}
      <div className="analytics-grid">
        <div className="stat-card">
          <div className="stat-icon">
            <i className="fas fa-eye"></i>
          </div>
          <div className="stat-info">
            <div className="stat-value">{visitorCount}</div>
            <div className="stat-label">Total Visits</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">
            <i className="fas fa-users"></i>
          </div>
          <div className="stat-info">
            <div className="stat-value">{visitorLogs.length}</div>
            <div className="stat-label">Tracked Visitors</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">
            <i className="fas fa-check-circle"></i>
          </div>
          <div className="stat-info">
            <div className="stat-value">{getTotalConversions()}</div>
            <div className="stat-label">Conversions</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">
            <i className="fas fa-percentage"></i>
          </div>
          <div className="stat-info">
            <div className="stat-value">
              {visitorCount > 0 ? ((getTotalConversions() / visitorCount) * 100).toFixed(2) : 0}%
            </div>
            <div className="stat-label">Conversion Rate</div>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="analytics-tabs">
        <button
          className={`tab ${selectedTab === 'overview' ? 'active' : ''}`}
          onClick={() => setSelectedTab('overview')}
        >
          <i className="fas fa-list"></i> Recent Visitors
        </button>
        <button
          className={`tab ${selectedTab === 'conversions' ? 'active' : ''}`}
          onClick={() => setSelectedTab('conversions')}
        >
          <i className="fas fa-handshake"></i> Conversions
        </button>
      </div>

      {/* Recent Visitors Table */}
      {selectedTab === 'overview' && (
        <div className="data-table-container">
          <h2>Recent Visitors ({visitorLogs.length})</h2>
          <table className="data-table">
            <thead>
              <tr>
                <th>Date & Time</th>
                <th>Device</th>
                <th>Browser</th>
                <th>Screen</th>
                <th>Page</th>
                <th>Referrer</th>
              </tr>
            </thead>
            <tbody>
              {visitorLogs.slice(0, 50).map((visit, index) => (
                <tr key={index}>
                  <td>{formatDate(visit.timestamp)}</td>
                  <td>
                    <i className={`fas ${getDeviceIcon(visit.userAgent)}`}></i>
                    {' '}{visit.screen.includes('Mobile') || visit.screen.split('x')[0] < 768 ? 'Mobile' : 'Desktop'}
                  </td>
                  <td>
                    <i className={`fab ${getBrowserIcon(visit.userAgent)}`}></i>
                  </td>
                  <td>{visit.screen}</td>
                  <td>{visit.page.replace('https://aadyaainfotech.in', '')}</td>
                  <td>{visit.referrer || 'Direct'}</td>
                </tr>
              ))}
            </tbody>
          </table>
          {visitorLogs.length === 0 && (
            <div className="empty-state">
              <i className="fas fa-inbox"></i>
              <p>No visitor data yet. Visitors will be tracked automatically.</p>
            </div>
          )}
        </div>
      )}

      {/* Conversions Table */}
      {selectedTab === 'conversions' && (
        <div className="data-table-container">
          <h2>Contact Form Submissions ({conversions.length})</h2>
          
          {/* Service Breakdown */}
          {conversions.length > 0 && (
            <div className="service-breakdown">
              <h3>Service Interest</h3>
              <div className="breakdown-grid">
                {Object.entries(getServiceBreakdown()).map(([service, count]) => (
                  <div key={service} className="breakdown-item">
                    <span className="service-name">{service}</span>
                    <span className="service-count">{count}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          <table className="data-table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Name</th>
                <th>Contact</th>
                <th>Service</th>
                <th>Message</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {conversions.map((conv, index) => (
                <tr key={index}>
                  <td>{formatDate(conv.timestamp)}</td>
                  <td>{conv.data?.name || 'N/A'}</td>
                  <td>
                    <div>{conv.data?.contact || 'N/A'}</div>
                  </td>
                  <td>
                    <span className="badge">{conv.data?.service}</span>
                  </td>
                  <td>{conv.data?.message?.substring(0, 50)}...</td>
                  <td>
                    <span className="status-badge status-new">New</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          {conversions.length === 0 && (
            <div className="empty-state">
              <i className="fas fa-inbox"></i>
              <p>No contact form submissions yet.</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default VisitorAnalytics;
