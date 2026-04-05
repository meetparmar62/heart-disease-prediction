import React, { useState } from 'react';

const InquiriesTracker = ({ inquiries, onUpdateStatus, onAddInquiry }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [filterStatus, setFilterStatus] = useState('all');
  const [formData, setFormData] = useState({
    name: '',
    contact: '',
    service: ''
  });

  const filteredInquiries = filterStatus === 'all' 
    ? inquiries 
    : inquiries.filter(i => i.status === filterStatus);

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddInquiry(formData);
    setIsModalOpen(false);
    setFormData({ name: '', contact: '', service: '' });
  };

  const getStatusColor = (status) => {
    switch(status) {
      case 'new': return '#10b981';
      case 'contacted': return '#3b82f6';
      case 'closed': return '#6b7280';
      default: return '#8b5cf6';
    }
  };

  return (
    <div className="inquiries-tracker">
      <div className="admin-header">
        <h1>Inquiries Management</h1>
        <button className="btn-add" onClick={() => setIsModalOpen(true)}>
          <i className="fas fa-plus"></i> Add Inquiry
        </button>
      </div>

      <div className="filter-tabs">
        <button 
          className={`filter-tab ${filterStatus === 'all' ? 'active' : ''}`}
          onClick={() => setFilterStatus('all')}
        >
          All ({inquiries.length})
        </button>
        <button 
          className={`filter-tab ${filterStatus === 'new' ? 'active' : ''}`}
          onClick={() => setFilterStatus('new')}
        >
          New ({inquiries.filter(i => i.status === 'new').length})
        </button>
        <button 
          className={`filter-tab ${filterStatus === 'contacted' ? 'active' : ''}`}
          onClick={() => setFilterStatus('contacted')}
        >
          Contacted ({inquiries.filter(i => i.status === 'contacted').length})
        </button>
        <button 
          className={`filter-tab ${filterStatus === 'closed' ? 'active' : ''}`}
          onClick={() => setFilterStatus('closed')}
        >
          Closed ({inquiries.filter(i => i.status === 'closed').length})
        </button>
      </div>

      <div className="inquiries-table">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Contact</th>
              <th>Service</th>
              <th>Date</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredInquiries.map(inquiry => (
              <tr key={inquiry.id}>
                <td>{inquiry.name}</td>
                <td>{inquiry.contact}</td>
                <td>{inquiry.service}</td>
                <td>{new Date(inquiry.date).toLocaleDateString()}</td>
                <td>
                  <span 
                    className="status-badge"
                    style={{ background: getStatusColor(inquiry.status) }}
                  >
                    {inquiry.status}
                  </span>
                </td>
                <td>
                  <select
                    value={inquiry.status}
                    onChange={(e) => onUpdateStatus(inquiry.id, e.target.value)}
                    className="status-select"
                  >
                    <option value="new">New</option>
                    <option value="contacted">Contacted</option>
                    <option value="closed">Closed</option>
                  </select>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        
        {filteredInquiries.length === 0 && (
          <p className="no-data">No inquiries found</p>
        )}
      </div>

      {isModalOpen && (
        <div className="modal-overlay" onClick={() => setIsModalOpen(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <h2>Add New Inquiry</h2>
              <button className="modal-close" onClick={() => setIsModalOpen(false)}>
                <i className="fas fa-times"></i>
              </button>
            </div>

            <form onSubmit={handleSubmit} className="inquiry-form">
              <div className="form-group">
                <label>Customer Name</label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label>Contact Number</label>
                <input
                  type="tel"
                  value={formData.contact}
                  onChange={(e) => setFormData({ ...formData, contact: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label>Service Interested In</label>
                <select
                  value={formData.service}
                  onChange={(e) => setFormData({ ...formData, service: e.target.value })}
                  required
                >
                  <option value="">Select Service</option>
                  <option value="Website Development">Website Development</option>
                  <option value="App Development">App Development</option>
                  <option value="SEO (Search Engine Optimization)">SEO (Search Engine Optimization)</option>
                  <option value="Digital Marketing">Digital Marketing</option>
                  <option value="Social Media Management">Social Media Management</option>
                  <option value="Branding & Design">Branding & Design</option>
                  <option value="AI Automation">AI Automation</option>
                </select>
              </div>

              <div className="modal-actions">
                <button type="button" className="btn-cancel" onClick={() => setIsModalOpen(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn-submit">
                  Add Inquiry
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default InquiriesTracker;
