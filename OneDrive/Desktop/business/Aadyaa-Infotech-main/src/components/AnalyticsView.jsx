import React from 'react';

const AnalyticsView = ({ services, inquiries }) => {
  const totalInquiries = inquiries.length;
  const newInquiries = inquiries.filter(i => i.status === 'new').length;
  const contactedInquiries = inquiries.filter(i => i.status === 'contacted').length;
  const closedInquiries = inquiries.filter(i => i.status === 'closed').length;

  // Calculate service-wise inquiries
  const serviceStats = services.map(service => {
    const count = inquiries.filter(i => i.service === service.title).length;
    return {
      name: service.title,
      icon: service.icon,
      count: count,
      percentage: totalInquiries > 0 ? Math.round((count / totalInquiries) * 100) : 0
    };
  });

  // Recent activity (last 7 days)
  const sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
  const recentInquiries = inquiries.filter(i => new Date(i.date) > sevenDaysAgo);

  return (
    <div className="analytics-view">
      <div className="admin-header">
        <h1>Analytics & Reports</h1>
        <p>Track your business performance and inquiries</p>
      </div>

      <div className="analytics-grid">
        <div className="analytics-card">
          <div className="card-icon" style={{ background: 'linear-gradient(135deg, #6366f1, #8b5cf6)' }}>
            <i className="fas fa-chart-pie"></i>
          </div>
          <div className="card-content">
            <h3>{totalInquiries}</h3>
            <p>Total Inquiries</p>
          </div>
        </div>

        <div className="analytics-card">
          <div className="card-icon" style={{ background: 'linear-gradient(135deg, #10b981, #3b82f6)' }}>
            <i className="fas fa-clock"></i>
          </div>
          <div className="card-content">
            <h3>{newInquiries}</h3>
            <p>Pending (New)</p>
          </div>
        </div>

        <div className="analytics-card">
          <div className="card-icon" style={{ background: 'linear-gradient(135deg, #3b82f6, #6366f1)' }}>
            <i className="fas fa-phone-alt"></i>
          </div>
          <div className="card-content">
            <h3>{contactedInquiries}</h3>
            <p>Contacted</p>
          </div>
        </div>

        <div className="analytics-card">
          <div className="card-icon" style={{ background: 'linear-gradient(135deg, #6b7280, #9ca3af)' }}>
            <i className="fas fa-check-circle"></i>
          </div>
          <div className="card-content">
            <h3>{closedInquiries}</h3>
            <p>Closed/Converted</p>
          </div>
        </div>
      </div>

      <div className="analytics-section">
        <h2>Service-Wise Inquiry Distribution</h2>
        <div className="service-stats">
          {serviceStats.map((stat, index) => (
            <div key={index} className="service-stat-item">
              <div className="stat-header">
                <div className="stat-service-info">
                  <i className={`fas ${stat.icon}`}></i>
                  <span>{stat.name}</span>
                </div>
                <div className="stat-numbers">
                  <span className="stat-count">{stat.count} inquiries</span>
                  <span className="stat-percent">{stat.percentage}%</span>
                </div>
              </div>
              <div className="progress-bar">
                <div 
                  className="progress-fill"
                  style={{ 
                    width: `${stat.percentage}%`,
                    background: `linear-gradient(135deg, hsl(${230 + index * 20}, 70%, 60%), hsl(${260 + index * 20}, 70%, 60%))`
                  }}
                ></div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="analytics-section">
        <h2>Recent Activity (Last 7 Days)</h2>
        <div className="activity-summary">
          <div className="summary-card">
            <h3>{recentInquiries.length}</h3>
            <p>New inquiries this week</p>
          </div>
          <div className="summary-card">
            <h3>{Math.round(recentInquiries.length / 7 * 10) / 10}</h3>
            <p>Average per day</p>
          </div>
          <div className="summary-card">
            <h3>{recentInquiries.filter(i => i.status === 'new').length}</h3>
            <p>Still pending</p>
          </div>
        </div>
      </div>

      <div className="analytics-section">
        <h2>Quick Insights</h2>
        <div className="insights-list">
          {totalInquiries === 0 ? (
            <p className="no-data">No data available yet. Start adding inquiries to see analytics.</p>
          ) : (
            <>
              <div className="insight-item">
                <i className="fas fa-lightbulb"></i>
                <div>
                  <h4>Conversion Rate</h4>
                  <p>{closedInquiries > 0 ? Math.round((closedInquiries / totalInquiries) * 100) : 0}% of total inquiries have been closed/converted</p>
                </div>
              </div>
              
              <div className="insight-item">
                <i className="fas fa-arrow-up"></i>
                <div>
                  <h4>Pending Follow-ups</h4>
                  <p>{newInquiries} inquiries need immediate attention</p>
                </div>
              </div>

              {serviceStats.sort((a, b) => b.count - a.count)[0]?.count > 0 && (
                <div className="insight-item">
                  <i className="fas fa-trophy"></i>
                  <div>
                    <h4>Most Popular Service</h4>
                    <p>{serviceStats.sort((a, b) => b.count - a.count)[0].name} with {serviceStats.sort((a, b) => b.count - a.count)[0].count} inquiries</p>
                  </div>
                </div>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default AnalyticsView;
