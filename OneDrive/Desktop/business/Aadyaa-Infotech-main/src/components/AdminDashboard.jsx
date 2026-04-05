import React, { useState, useEffect } from 'react';
import AdminSidebar from './AdminSidebar';
import DashboardHome from './DashboardHome';
import ServicesManager from './ServicesManager';
import InquiriesTracker from './InquiriesTracker';
import AnalyticsView from './AnalyticsView';
import ProjectsManager from './ProjectsManager';
import TeamManager from './TeamManager';
import TestimonialsManager from './TestimonialsManager';
import WebsiteSettings from './WebsiteSettings';
import VisitorAnalytics from './VisitorAnalytics';

const AdminDashboard = ({ user, onLogout }) => {
  const [activeSection, setActiveSection] = useState('dashboard');
  const [services, setServices] = useState([]);
  const [inquiries, setInquiries] = useState([]);

  useEffect(() => {
    // Load services from localStorage or use ALL 7 default services from website
    const storedServices = localStorage.getItem('services');
    if (storedServices) {
      setServices(JSON.parse(storedServices));
    } else {
      // All 7 Aadyaa Infotech services
      const allDefaultServices = [
        {
          title: "Website Development",
          icon: "fa-laptop-code",
          desc: "Professional websites that work 24/7 to sell your services while you sleep. Fast, SEO-ready sites that convert visitors into customers.",
          features: [
            "Business Website (Static & Dynamic)",
            "E-commerce Website",
            "Custom Web Solutions",
            "Mobile-First Responsiveness",
            "Technical SEO Architecture",
            "Lightning Fast Page Loading"
          ]
        },
        {
          title: "App Development",
          icon: "fa-mobile-alt",
          desc: "Put your business in your customers' pocket. Native iOS and Android apps or cross-platform solutions that engage users.",
          features: [
            "Android & iOS Apps",
            "Service / Booking Apps",
            "Custom Business Apps",
            "Native App Development",
            "Cross-Platform Solutions",
            "App Store Publishing Support"
          ]
        },
        {
          title: "SEO (Search Engine Optimization)",
          icon: "fa-search",
          desc: "Improve your Google ranking and get found by more customers. Comprehensive SEO strategies that drive organic traffic.",
          features: [
            "Google Ranking Improvement",
            "Keyword Optimization",
            "On-page & Off-page SEO",
            "Technical SEO Audit",
            "Content Optimization",
            "Link Building Strategies"
          ]
        },
        {
          title: "Digital Marketing",
          icon: "fa-bullhorn",
          desc: "Reach more customers with data-driven marketing campaigns. Measurable results across all digital channels.",
          features: [
            "Google Ads",
            "Meta Ads (Facebook & Instagram)",
            "Lead Generation Campaigns",
            "PPC Management",
            "Retargeting Campaigns",
            "Performance Tracking & Analytics"
          ]
        },
        {
          title: "Social Media Management",
          icon: "fa-hashtag",
          desc: "Grow your online presence with engaging content and strategic management across all social platforms.",
          features: [
            "Instagram Growth",
            "Content Creation (Posts, Reels)",
            "Page Handling & Strategy",
            "Community Management",
            "Influencer Collaboration",
            "Social Media Analytics"
          ]
        },
        {
          title: "Branding & Design",
          icon: "fa-paint-brush",
          desc: "Create a stunning brand identity that captivates your audience and stands out from the competition.",
          features: [
            "Logo Design",
            "Posters & Creatives",
            "UI/UX Design",
            "Brand Identity Development",
            "Visual Style Guides",
            "Marketing Material Design"
          ]
        },
        {
          title: "AI Automation",
          icon: "fa-robot",
          desc: "Transform your business with intelligent AI solutions that automate tasks, reduce costs, and boost productivity 24/7.",
          features: [
            "AI Chatbots (Website + WhatsApp Auto Reply)",
            "Lead Automation System (Auto Capture & Follow-up)",
            "Email & WhatsApp Marketing Automation",
            "CRM Automation (Customer Data Management)",
            "AI-based Customer Support (24/7 Response)",
            "Sales Funnel Automation",
            "AI Content Generation (Posts, Ads, Scripts)",
            "Workflow Automation (Business Process Auto)"
          ]
        }
      ];
      setServices(allDefaultServices);
      localStorage.setItem('services', JSON.stringify(allDefaultServices));
    }

    // Load inquiries
    const storedInquiries = localStorage.getItem('inquiries');
    if (storedInquiries) {
      setInquiries(JSON.parse(storedInquiries));
    } else {
      // Sample inquiries for demo
      const sampleInquiries = [
        { id: 1, service: 'Business Websites', name: 'John Doe', contact: '+91 9876543210', date: new Date().toISOString(), status: 'new' },
        { id: 2, service: 'Ecommerce Development', name: 'Jane Smith', contact: '+91 9876543211', date: new Date(Date.now() - 86400000).toISOString(), status: 'contacted' },
        { id: 3, service: 'Mobile App Development', name: 'Mike Johnson', contact: '+91 9876543212', date: new Date(Date.now() - 172800000).toISOString(), status: 'closed' }
      ];
      setInquiries(sampleInquiries);
      localStorage.setItem('inquiries', JSON.stringify(sampleInquiries));
    }
  }, []);

  const addService = (service) => {
    const updatedServices = [...services, service];
    setServices(updatedServices);
    localStorage.setItem('services', JSON.stringify(updatedServices));
  };

  const updateService = (index, updatedService) => {
    const updatedServices = [...services];
    updatedServices[index] = updatedService;
    setServices(updatedServices);
    localStorage.setItem('services', JSON.stringify(updatedServices));
  };

  const deleteService = (index) => {
    const updatedServices = services.filter((_, i) => i !== index);
    setServices(updatedServices);
    localStorage.setItem('services', JSON.stringify(updatedServices));
  };

  const addInquiry = (inquiry) => {
    const updatedInquiries = [...inquiries, { ...inquiry, id: Date.now(), date: new Date().toISOString(), status: 'new' }];
    setInquiries(updatedInquiries);
    localStorage.setItem('inquiries', JSON.stringify(updatedInquiries));
  };

  const updateInquiryStatus = (id, status) => {
    const updatedInquiries = inquiries.map(inq => 
      inq.id === id ? { ...inq, status } : inq
    );
    setInquiries(updatedInquiries);
    localStorage.setItem('inquiries', JSON.stringify(updatedInquiries));
  };

  const renderContent = () => {
    switch(activeSection) {
      case 'dashboard':
        return <DashboardHome services={services} inquiries={inquiries} />;
      case 'services':
        return <ServicesManager 
          services={services} 
          onAdd={addService} 
          onUpdate={updateService} 
          onDelete={deleteService} 
        />;
      case 'inquiries':
        return <InquiriesTracker 
          inquiries={inquiries} 
          onUpdateStatus={updateInquiryStatus}
          onAddInquiry={addInquiry}
        />;
      case 'analytics':
        return <VisitorAnalytics />;
      case 'projects':
        return <ProjectsManager />;
      case 'team':
        return <TeamManager />;
      case 'testimonials':
        return <TestimonialsManager />;
      case 'settings':
        return <WebsiteSettings />;
      default:
        return <DashboardHome services={services} inquiries={inquiries} />;
    }
  };

  return (
    <div className="admin-dashboard">
      <AdminSidebar 
        activeSection={activeSection} 
        onSectionChange={setActiveSection} 
        onLogout={onLogout}
        user={user}
      />
      <div className="admin-content">
        {renderContent()}
      </div>
    </div>
  );
};

export default AdminDashboard;
