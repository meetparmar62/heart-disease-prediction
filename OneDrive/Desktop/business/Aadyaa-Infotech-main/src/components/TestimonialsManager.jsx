import React, { useState } from 'react';

const TestimonialsManager = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingIndex, setEditingIndex] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    role: '',
    company: '',
    testimonial: '',
    rating: 5,
    image: ''
  });

  const [testimonials, setTestimonials] = useState(() => {
    const stored = localStorage.getItem('testimonials');
    return stored ? JSON.parse(stored) : [];
  });

  const openModal = (index = null) => {
    if (index !== null) {
      setEditingIndex(index);
      setFormData(testimonials[index]);
    } else {
      setEditingIndex(null);
      setFormData({
        name: '',
        role: '',
        company: '',
        testimonial: '',
        rating: 5,
        image: ''
      });
    }
    setIsModalOpen(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingIndex !== null) {
      const updated = [...testimonials];
      updated[editingIndex] = formData;
      setTestimonials(updated);
      localStorage.setItem('testimonials', JSON.stringify(updated));
    } else {
      const updated = [...testimonials, formData];
      setTestimonials(updated);
      localStorage.setItem('testimonials', JSON.stringify(updated));
    }
    setIsModalOpen(false);
  };

  const deleteTestimonial = (index) => {
    if (window.confirm('Are you sure you want to delete this testimonial?')) {
      const updated = testimonials.filter((_, i) => i !== index);
      setTestimonials(updated);
      localStorage.setItem('testimonials', JSON.stringify(updated));
    }
  };

  const renderStars = (rating) => {
    return (
      <div className="star-rating">
        {[...Array(5)].map((_, i) => (
          <i 
            key={i} 
            className={`fas fa-star ${i < rating ? 'filled' : ''}`}
            style={{ color: i < rating ? '#fbbf24' : '#d1d5db' }}
          ></i>
        ))}
      </div>
    );
  };

  return (
    <div className="testimonials-manager">
      <div className="admin-header">
        <h1>Clients Testimonials Management</h1>
        <button className="btn-add" onClick={() => openModal()}>
          <i className="fas fa-plus"></i> Add Testimonial
        </button>
      </div>

      <div className="testimonials-list">
        {testimonials.length === 0 ? (
          <p className="no-data">No testimonials added yet.</p>
        ) : (
          testimonials.map((testimonial, index) => (
            <div key={index} className="testimonial-item">
              <div className="testimonial-content">
                {testimonial.image && (
                  <img src={testimonial.image} alt={testimonial.name} className="testimonial-image" />
                )}
                <div className="testimonial-text">
                  <div className="testimonial-header">
                    <div>
                      <h3>{testimonial.name}</h3>
                      <p className="testimonial-role">{testimonial.role} at {testimonial.company}</p>
                    </div>
                    {renderStars(testimonial.rating)}
                  </div>
                  <p className="testimonial-quote">"{testimonial.testimonial}"</p>
                </div>
              </div>
              <div className="service-actions">
                <button className="btn-edit" onClick={() => openModal(index)}>
                  <i className="fas fa-edit"></i>
                </button>
                <button className="btn-delete" onClick={() => deleteTestimonial(index)}>
                  <i className="fas fa-trash"></i>
                </button>
              </div>
            </div>
          ))
        )}
      </div>

      {isModalOpen && (
        <div className="modal-overlay" onClick={() => setIsModalOpen(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <h2>{editingIndex !== null ? 'Edit Testimonial' : 'Add Testimonial'}</h2>
              <button className="modal-close" onClick={() => setIsModalOpen(false)}>
                <i className="fas fa-times"></i>
              </button>
            </div>

            <form onSubmit={handleSubmit} className="service-form">
              <div className="form-group">
                <label>Client Name</label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label>Role/Position</label>
                <input
                  type="text"
                  value={formData.role}
                  onChange={(e) => setFormData({ ...formData, role: e.target.value })}
                  placeholder="e.g., CEO, Marketing Director"
                  required
                />
              </div>

              <div className="form-group">
                <label>Company</label>
                <input
                  type="text"
                  value={formData.company}
                  onChange={(e) => setFormData({ ...formData, company: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label>Image URL (Optional)</label>
                <input
                  type="url"
                  value={formData.image}
                  onChange={(e) => setFormData({ ...formData, image: e.target.value })}
                  placeholder="https://example.com/photo.jpg"
                />
              </div>

              <div className="form-group">
                <label>Rating</label>
                <select
                  value={formData.rating}
                  onChange={(e) => setFormData({ ...formData, rating: parseInt(e.target.value) })}
                >
                  <option value="5">⭐⭐⭐⭐⭐ (5 Stars)</option>
                  <option value="4">⭐⭐⭐⭐ (4 Stars)</option>
                  <option value="3">⭐⭐⭐ (3 Stars)</option>
                  <option value="2">⭐⭐ (2 Stars)</option>
                  <option value="1">⭐ (1 Star)</option>
                </select>
              </div>

              <div className="form-group">
                <label>Testimonial</label>
                <textarea
                  value={formData.testimonial}
                  onChange={(e) => setFormData({ ...formData, testimonial: e.target.value })}
                  rows="5"
                  placeholder="Client's feedback about your services..."
                  required
                />
              </div>

              <div className="modal-actions">
                <button type="button" className="btn-cancel" onClick={() => setIsModalOpen(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn-submit">
                  {editingIndex !== null ? 'Update' : 'Add'} Testimonial
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default TestimonialsManager;
