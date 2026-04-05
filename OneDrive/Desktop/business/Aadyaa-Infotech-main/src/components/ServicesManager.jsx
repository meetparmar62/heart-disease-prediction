import React, { useState } from 'react';

const ServicesManager = ({ services, onAdd, onUpdate, onDelete }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingIndex, setEditingIndex] = useState(null);
  const [formData, setFormData] = useState({
    title: '',
    icon: 'fa-laptop-code',
    desc: '',
    features: ['']
  });

  const openModal = (index = null) => {
    if (index !== null) {
      setEditingIndex(index);
      setFormData(services[index]);
    } else {
      setEditingIndex(null);
      setFormData({
        title: '',
        icon: 'fa-laptop-code',
        desc: '',
        features: ['']
      });
    }
    setIsModalOpen(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingIndex !== null) {
      onUpdate(editingIndex, formData);
    } else {
      onAdd(formData);
    }
    setIsModalOpen(false);
  };

  const addFeature = () => {
    setFormData({ ...formData, features: [...formData.features, ''] });
  };

  const removeFeature = (index) => {
    const updatedFeatures = formData.features.filter((_, i) => i !== index);
    setFormData({ ...formData, features: updatedFeatures });
  };

  const updateFeature = (index, value) => {
    const updatedFeatures = [...formData.features];
    updatedFeatures[index] = value;
    setFormData({ ...formData, features: updatedFeatures });
  };

  return (
    <div className="services-manager">
      <div className="admin-header">
        <h1>Services Management</h1>
        <button className="btn-add" onClick={() => openModal()}>
          <i className="fas fa-plus"></i> Add Service
        </button>
      </div>

      <div className="services-list">
        {services.map((service, index) => (
          <div key={index} className="service-item">
            <div className="service-icon">
              <i className={`fas ${service.icon}`}></i>
            </div>
            <div className="service-info">
              <h3>{service.title}</h3>
              <p>{service.desc}</p>
              <div className="service-features-preview">
                {service.features.slice(0, 3).map((feature, i) => (
                  <span key={i} className="feature-tag">{feature}</span>
                ))}
                {service.features.length > 3 && (
                  <span className="feature-more">+{service.features.length - 3} more</span>
                )}
              </div>
            </div>
            <div className="service-actions">
              <button className="btn-edit" onClick={() => openModal(index)}>
                <i className="fas fa-edit"></i>
              </button>
              <button className="btn-delete" onClick={() => onDelete(index)}>
                <i className="fas fa-trash"></i>
              </button>
            </div>
          </div>
        ))}
      </div>

      {isModalOpen && (
        <div className="modal-overlay" onClick={() => setIsModalOpen(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <h2>{editingIndex !== null ? 'Edit Service' : 'Add New Service'}</h2>
              <button className="modal-close" onClick={() => setIsModalOpen(false)}>
                <i className="fas fa-times"></i>
              </button>
            </div>

            <form onSubmit={handleSubmit} className="service-form">
              <div className="form-group">
                <label>Service Title</label>
                <input
                  type="text"
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label>Icon Class</label>
                <select
                  value={formData.icon}
                  onChange={(e) => setFormData({ ...formData, icon: e.target.value })}
                >
                  <option value="fa-laptop-code">fa-laptop-code</option>
                  <option value="fa-shopping-cart">fa-shopping-cart</option>
                  <option value="fa-mobile-alt">fa-mobile-alt</option>
                  <option value="fa-edit">fa-edit</option>
                  <option value="fa-rocket">fa-rocket</option>
                  <option value="fa-cogs">fa-cogs</option>
                  <option value="fa-brain">fa-brain</option>
                  <option value="fa-bullhorn">fa-bullhorn</option>
                  <option value="fa-paint-brush">fa-paint-brush</option>
                  <option value="fa-cloud">fa-cloud</option>
                  <option value="fa-code-branch">fa-code-branch</option>
                </select>
              </div>

              <div className="form-group">
                <label>Description</label>
                <textarea
                  value={formData.desc}
                  onChange={(e) => setFormData({ ...formData, desc: e.target.value })}
                  rows="4"
                  required
                />
              </div>

              <div className="form-group">
                <label>Features</label>
                {formData.features.map((feature, index) => (
                  <div key={index} className="feature-input-group">
                    <input
                      type="text"
                      value={feature}
                      onChange={(e) => updateFeature(index, e.target.value)}
                      placeholder={`Feature ${index + 1}`}
                    />
                    <button
                      type="button"
                      className="btn-remove-feature"
                      onClick={() => removeFeature(index)}
                    >
                      <i className="fas fa-times"></i>
                    </button>
                  </div>
                ))}
                <button type="button" className="btn-add-feature" onClick={addFeature}>
                  <i className="fas fa-plus"></i> Add Feature
                </button>
              </div>

              <div className="modal-actions">
                <button type="button" className="btn-cancel" onClick={() => setIsModalOpen(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn-submit">
                  {editingIndex !== null ? 'Update' : 'Create'} Service
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default ServicesManager;
