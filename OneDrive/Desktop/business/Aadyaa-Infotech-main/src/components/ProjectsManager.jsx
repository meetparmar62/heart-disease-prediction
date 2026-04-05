import React, { useState } from 'react';

const ProjectsManager = ({ onAddProject, onUpdateProject, onDeleteProject }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingIndex, setEditingIndex] = useState(null);
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    image: '',
    tags: [''],
    link: ''
  });

  // Load projects from localStorage
  const [projects, setProjects] = useState(() => {
    const stored = localStorage.getItem('projects');
    return stored ? JSON.parse(stored) : [];
  });

  const openModal = (index = null) => {
    if (index !== null) {
      setEditingIndex(index);
      setFormData(projects[index]);
    } else {
      setEditingIndex(null);
      setFormData({
        title: '',
        description: '',
        image: '',
        tags: [''],
        link: ''
      });
    }
    setIsModalOpen(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingIndex !== null) {
      const updated = [...projects];
      updated[editingIndex] = formData;
      setProjects(updated);
      localStorage.setItem('projects', JSON.stringify(updated));
      if (onUpdateProject) onUpdateProject(updated);
    } else {
      const updated = [...projects, formData];
      setProjects(updated);
      localStorage.setItem('projects', JSON.stringify(updated));
      if (onAddProject) onAddProject(updated);
    }
    setIsModalOpen(false);
  };

  const addTag = () => {
    setFormData({ ...formData, tags: [...formData.tags, ''] });
  };

  const removeTag = (index) => {
    const updated = formData.tags.filter((_, i) => i !== index);
    setFormData({ ...formData, tags: updated });
  };

  const updateTag = (index, value) => {
    const updated = [...formData.tags];
    updated[index] = value;
    setFormData({ ...formData, tags: updated });
  };

  const deleteProject = (index) => {
    if (window.confirm('Are you sure you want to delete this project?')) {
      const updated = projects.filter((_, i) => i !== index);
      setProjects(updated);
      localStorage.setItem('projects', JSON.stringify(updated));
      if (onDeleteProject) onDeleteProject(updated);
    }
  };

  return (
    <div className="projects-manager">
      <div className="admin-header">
        <h1>Portfolio/Projects Management</h1>
        <button className="btn-add" onClick={() => openModal()}>
          <i className="fas fa-plus"></i> Add Project
        </button>
      </div>

      <div className="projects-list">
        {projects.length === 0 ? (
          <p className="no-data">No projects added yet. Click "Add Project" to get started!</p>
        ) : (
          projects.map((project, index) => (
            <div key={index} className="project-item">
              {project.image && (
                <div className="project-image-preview">
                  <img src={project.image} alt={project.title} />
                </div>
              )}
              <div className="project-info">
                <h3>{project.title}</h3>
                <p>{project.description}</p>
                <div className="project-tags">
                  {project.tags.filter(t => t).map((tag, i) => (
                    <span key={i} className="feature-tag">{tag}</span>
                  ))}
                </div>
                {project.link && (
                  <a href={project.link} target="_blank" rel="noopener noreferrer" className="project-link">
                    <i className="fas fa-external-link-alt"></i> Visit Project
                  </a>
                )}
              </div>
              <div className="service-actions">
                <button className="btn-edit" onClick={() => openModal(index)}>
                  <i className="fas fa-edit"></i>
                </button>
                <button className="btn-delete" onClick={() => deleteProject(index)}>
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
              <h2>{editingIndex !== null ? 'Edit Project' : 'Add New Project'}</h2>
              <button className="modal-close" onClick={() => setIsModalOpen(false)}>
                <i className="fas fa-times"></i>
              </button>
            </div>

            <form onSubmit={handleSubmit} className="service-form">
              <div className="form-group">
                <label>Project Title</label>
                <input
                  type="text"
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label>Description</label>
                <textarea
                  value={formData.description}
                  onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                  rows="4"
                  required
                />
              </div>

              <div className="form-group">
                <label>Image URL</label>
                <input
                  type="url"
                  value={formData.image}
                  onChange={(e) => setFormData({ ...formData, image: e.target.value })}
                  placeholder="https://example.com/image.jpg"
                />
              </div>

              <div className="form-group">
                <label>Project Link (Optional)</label>
                <input
                  type="url"
                  value={formData.link}
                  onChange={(e) => setFormData({ ...formData, link: e.target.value })}
                  placeholder="https://example.com"
                />
              </div>

              <div className="form-group">
                <label>Tags</label>
                {formData.tags.map((tag, index) => (
                  <div key={index} className="feature-input-group">
                    <input
                      type="text"
                      value={tag}
                      onChange={(e) => updateTag(index, e.target.value)}
                      placeholder={`Tag ${index + 1}`}
                    />
                    <button
                      type="button"
                      className="btn-remove-feature"
                      onClick={() => removeTag(index)}
                    >
                      <i className="fas fa-times"></i>
                    </button>
                  </div>
                ))}
                <button type="button" className="btn-add-feature" onClick={addTag}>
                  <i className="fas fa-plus"></i> Add Tag
                </button>
              </div>

              <div className="modal-actions">
                <button type="button" className="btn-cancel" onClick={() => setIsModalOpen(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn-submit">
                  {editingIndex !== null ? 'Update' : 'Create'} Project
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProjectsManager;
