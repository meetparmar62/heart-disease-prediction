import React, { useState } from 'react';

const WebsiteSettings = () => {
  const [settings, setSettings] = useState(() => {
    const stored = localStorage.getItem('websiteSettings');
    return stored ? JSON.parse(stored) : {
      siteTitle: 'Aadyaa Infotech',
      siteDescription: 'Creative Digital Solutions',
      contactEmail: 'info@aadyaainfotech.com',
      contactPhone: '+91 6355893624',
      whatsappNumber: '916355893624',
      address: 'India',
      socialLinks: {
        facebook: '',
        twitter: '',
        instagram: '',
        linkedin: '',
        github: ''
      },
      seoKeywords: 'web development, app development, digital marketing, SEO',
      googleAnalytics: '',
      customCSS: ''
    };
  });

  const [activeTab, setActiveTab] = useState('general');

  const handleSave = () => {
    localStorage.setItem('websiteSettings', JSON.stringify(settings));
    alert('Settings saved successfully! 🎉');
  };

  const tabs = [
    { id: 'general', label: 'General', icon: 'fa-cog' },
    { id: 'contact', label: 'Contact Info', icon: 'fa-address-book' },
    { id: 'social', label: 'Social Media', icon: 'fa-share-alt' },
    { id: 'seo', label: 'SEO & Analytics', icon: 'fa-chart-line' }
  ];

  return (
    <div className="website-settings">
      <div className="admin-header">
        <h1>Website Settings & Configuration</h1>
        <button className="btn-submit" onClick={handleSave}>
          <i className="fas fa-save"></i> Save Settings
        </button>
      </div>

      <div className="settings-tabs">
        {tabs.map(tab => (
          <button
            key={tab.id}
            className={`settings-tab ${activeTab === tab.id ? 'active' : ''}`}
            onClick={() => setActiveTab(tab.id)}
          >
            <i className={`fas ${tab.icon}`}></i>
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      <div className="settings-content">
        {activeTab === 'general' && (
          <div className="settings-section">
            <h2>General Information</h2>
            
            <div className="form-group">
              <label>Website Title</label>
              <input
                type="text"
                value={settings.siteTitle}
                onChange={(e) => setSettings({ ...settings, siteTitle: e.target.value })}
                placeholder="Your website title"
              />
            </div>

            <div className="form-group">
              <label>Website Description</label>
              <textarea
                value={settings.siteDescription}
                onChange={(e) => setSettings({ ...settings, siteDescription: e.target.value })}
                rows="3"
                placeholder="Brief description of your website"
              />
            </div>

            <div className="form-group">
              <label>Business Address</label>
              <input
                type="text"
                value={settings.address}
                onChange={(e) => setSettings({ ...settings, address: e.target.value })}
                placeholder="Your business address"
              />
            </div>
          </div>
        )}

        {activeTab === 'contact' && (
          <div className="settings-section">
            <h2>Contact Information</h2>
            
            <div className="form-group">
              <label>Contact Email</label>
              <input
                type="email"
                value={settings.contactEmail}
                onChange={(e) => setSettings({ ...settings, contactEmail: e.target.value })}
                placeholder="your@email.com"
              />
            </div>

            <div className="form-group">
              <label>Contact Phone</label>
              <input
                type="tel"
                value={settings.contactPhone}
                onChange={(e) => setSettings({ ...settings, contactPhone: e.target.value })}
                placeholder="+91 XXXXXXXXXX"
              />
            </div>

            <div className="form-group">
              <label>WhatsApp Number (with country code)</label>
              <input
                type="tel"
                value={settings.whatsappNumber}
                onChange={(e) => setSettings({ ...settings, whatsappNumber: e.target.value })}
                placeholder="91XXXXXXXXXX"
              />
              <small>Format: 916355893624 (no + or spaces)</small>
            </div>
          </div>
        )}

        {activeTab === 'social' && (
          <div className="settings-section">
            <h2>Social Media Links</h2>
            
            <div className="form-group">
              <label>Facebook Page URL</label>
              <input
                type="url"
                value={settings.socialLinks.facebook}
                onChange={(e) => setSettings({ 
                  ...settings, 
                  socialLinks: { ...settings.socialLinks, facebook: e.target.value } 
                })}
                placeholder="https://facebook.com/yourpage"
              />
            </div>

            <div className="form-group">
              <label>Twitter Profile URL</label>
              <input
                type="url"
                value={settings.socialLinks.twitter}
                onChange={(e) => setSettings({ 
                  ...settings, 
                  socialLinks: { ...settings.socialLinks, twitter: e.target.value } 
                })}
                placeholder="https://twitter.com/yourprofile"
              />
            </div>

            <div className="form-group">
              <label>Instagram Profile URL</label>
              <input
                type="url"
                value={settings.socialLinks.instagram}
                onChange={(e) => setSettings({ 
                  ...settings, 
                  socialLinks: { ...settings.socialLinks, instagram: e.target.value } 
                })}
                placeholder="https://instagram.com/yourprofile"
              />
            </div>

            <div className="form-group">
              <label>LinkedIn Company URL</label>
              <input
                type="url"
                value={settings.socialLinks.linkedin}
                onChange={(e) => setSettings({ 
                  ...settings, 
                  socialLinks: { ...settings.socialLinks, linkedin: e.target.value } 
                })}
                placeholder="https://linkedin.com/company/yourcompany"
              />
            </div>

            <div className="form-group">
              <label>GitHub Organization URL</label>
              <input
                type="url"
                value={settings.socialLinks.github}
                onChange={(e) => setSettings({ 
                  ...settings, 
                  socialLinks: { ...settings.socialLinks, github: e.target.value } 
                })}
                placeholder="https://github.com/yourorg"
              />
            </div>
          </div>
        )}

        {activeTab === 'seo' && (
          <div className="settings-section">
            <h2>SEO & Analytics</h2>
            
            <div className="form-group">
              <label>SEO Keywords (comma-separated)</label>
              <textarea
                value={settings.seoKeywords}
                onChange={(e) => setSettings({ ...settings, seoKeywords: e.target.value })}
                rows="3"
                placeholder="web development, app development, digital marketing"
              />
            </div>

            <div className="form-group">
              <label>Google Analytics Tracking ID</label>
              <input
                type="text"
                value={settings.googleAnalytics}
                onChange={(e) => setSettings({ ...settings, googleAnalytics: e.target.value })}
                placeholder="UA-XXXXXXXXX-X or G-XXXXXXXXXX"
              />
              <small>Enter your GA4 or Universal Analytics tracking ID</small>
            </div>

            <div className="form-group">
              <label>Custom CSS (Advanced)</label>
              <textarea
                value={settings.customCSS}
                onChange={(e) => setSettings({ ...settings, customCSS: e.target.value })}
                rows="6"
                placeholder="Add your custom CSS here..."
                style={{ fontFamily: 'monospace', fontSize: '0.85rem' }}
              />
              <small>⚠️ Use with caution. Invalid CSS may break your site.</small>
            </div>
          </div>
        )}
      </div>

      <div className="settings-footer">
        <button className="btn-submit" onClick={handleSave}>
          <i className="fas fa-save"></i> Save All Settings
        </button>
        <p>Changes are saved to localStorage and will persist across sessions.</p>
      </div>
    </div>
  );
};

export default WebsiteSettings;
