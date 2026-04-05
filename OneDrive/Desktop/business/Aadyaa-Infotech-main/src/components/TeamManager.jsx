import React, { useState } from 'react';

const TeamManager = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingIndex, setEditingIndex] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    role: '',
    image: '',
    bio: '',
    social: {
      linkedin: '',
      twitter: '',
      github: ''
    }
  });

  const [teamMembers, setTeamMembers] = useState(() => {
    const stored = localStorage.getItem('teamMembers');
    return stored ? JSON.parse(stored) : [];
  });

  const openModal = (index = null) => {
    if (index !== null) {
      setEditingIndex(index);
      setFormData(teamMembers[index]);
    } else {
      setEditingIndex(null);
      setFormData({
        name: '',
        role: '',
        image: '',
        bio: '',
        social: {
          linkedin: '',
          twitter: '',
          github: ''
        }
      });
    }
    setIsModalOpen(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingIndex !== null) {
      const updated = [...teamMembers];
      updated[editingIndex] = formData;
      setTeamMembers(updated);
      localStorage.setItem('teamMembers', JSON.stringify(updated));
    } else {
      const updated = [...teamMembers, formData];
      setTeamMembers(updated);
      localStorage.setItem('teamMembers', JSON.stringify(updated));
    }
    setIsModalOpen(false);
  };

  const deleteMember = (index) => {
    if (window.confirm('Are you sure you want to remove this team member?')) {
      const updated = teamMembers.filter((_, i) => i !== index);
      setTeamMembers(updated);
      localStorage.setItem('teamMembers', JSON.stringify(updated));
    }
  };

  return (
    <div className="team-manager">
      <div className="admin-header">
        <h1>Team Members Management</h1>
        <button className="btn-add" onClick={() => openModal()}>
          <i className="fas fa-plus"></i> Add Team Member
        </button>
      </div>

      <div className="team-list">
        {teamMembers.length === 0 ? (
          <p className="no-data">No team members added yet.</p>
        ) : (
          teamMembers.map((member, index) => (
            <div key={index} className="team-member-item">
              {member.image && (
                <div className="member-image-preview">
                  <img src={member.image} alt={member.name} />
                </div>
              )}
              <div className="member-info">
                <h3>{member.name}</h3>
                <p className="member-role">{member.role}</p>
                <p className="member-bio">{member.bio}</p>
                <div className="member-social">
                  {member.social.linkedin && (
                    <span className="social-tag"><i className="fab fa-linkedin"></i> LinkedIn</span>
                  )}
                  {member.social.twitter && (
                    <span className="social-tag"><i className="fab fa-twitter"></i> Twitter</span>
                  )}
                  {member.social.github && (
                    <span className="social-tag"><i className="fab fa-github"></i> GitHub</span>
                  )}
                </div>
              </div>
              <div className="service-actions">
                <button className="btn-edit" onClick={() => openModal(index)}>
                  <i className="fas fa-edit"></i>
                </button>
                <button className="btn-delete" onClick={() => deleteMember(index)}>
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
              <h2>{editingIndex !== null ? 'Edit Team Member' : 'Add Team Member'}</h2>
              <button className="modal-close" onClick={() => setIsModalOpen(false)}>
                <i className="fas fa-times"></i>
              </button>
            </div>

            <form onSubmit={handleSubmit} className="service-form">
              <div className="form-group">
                <label>Full Name</label>
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
                  placeholder="e.g., Senior Developer, UI Designer"
                  required
                />
              </div>

              <div className="form-group">
                <label>Image URL</label>
                <input
                  type="url"
                  value={formData.image}
                  onChange={(e) => setFormData({ ...formData, image: e.target.value })}
                  placeholder="https://example.com/photo.jpg"
                />
              </div>

              <div className="form-group">
                <label>Bio/Description</label>
                <textarea
                  value={formData.bio}
                  onChange={(e) => setFormData({ ...formData, bio: e.target.value })}
                  rows="4"
                  placeholder="Brief description about the team member..."
                />
              </div>

              <div className="form-group">
                <label>Social Media Links (Optional)</label>
                <div className="social-inputs">
                  <input
                    type="url"
                    placeholder="LinkedIn Profile URL"
                    value={formData.social.linkedin}
                    onChange={(e) => setFormData({ 
                      ...formData, 
                      social: { ...formData.social, linkedin: e.target.value } 
                    })}
                  />
                  <input
                    type="url"
                    placeholder="Twitter Profile URL"
                    value={formData.social.twitter}
                    onChange={(e) => setFormData({ 
                      ...formData, 
                      social: { ...formData.social, twitter: e.target.value } 
                    })}
                  />
                  <input
                    type="url"
                    placeholder="GitHub Profile URL"
                    value={formData.social.github}
                    onChange={(e) => setFormData({ 
                      ...formData, 
                      social: { ...formData.social, github: e.target.value } 
                    })}
                  />
                </div>
              </div>

              <div className="modal-actions">
                <button type="button" className="btn-cancel" onClick={() => setIsModalOpen(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn-submit">
                  {editingIndex !== null ? 'Update' : 'Add'} Team Member
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default TeamManager;
