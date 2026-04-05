import React, { useEffect, useRef } from 'react';

const projects = [
    {
        name: "Aadyaa Infotech Corporate Website",
        category: "Business Website",
        description: "Professional digital presence for a leading IT services company",
        image: "/1.png",
        features: [
            { icon: "fa-laptop-code", text: "Modern Design" },
            { icon: "fa-mobile-alt", text: "Responsive Layout" }
        ]
    },
    {
        name: "Aadyaa Business Mobile App",
        category: "Mobile Application",
        description: "Connecting businesses to customers through innovative mobile solutions",
        image: "/2.png",
        features: [
            { icon: "fa-mobile-alt", text: "Cross-Platform" },
            { icon: "fa-bolt", text: "Fast Performance" }
        ]
    },
    {
        name: "Aadyaa Services Portal",
        category: "Web Portal",
        description: "Comprehensive service showcase and client engagement platform",
        image: "/3.png",
        features: [
            { icon: "fa-paint-brush", text: "UI/UX Design" },
            { icon: "fa-chart-line", text: "SEO Optimized" }
        ]
    },
    {
        name: "Ecommerce Platform Dashboard",
        category: "Ecommerce",
        description: "Advanced analytics and inventory management system for online retail",
        image: "/4.png",
        features: [
            { icon: "fa-chart-pie", text: "Real-time Analytics" },
            { icon: "fa-database", text: "Inventory Management" }
        ]
    },
    {
        name: "Healthcare Practice Management",
        category: "Healthcare IT",
        description: "Digital patient care and appointment scheduling solution",
        image: "/5.png",
        features: [
            { icon: "fa-heartbeat", text: "Patient Tracking" },
            { icon: "fa-calendar-check", text: "Smart Scheduling" }
        ]
    },
    {
        name: "Professional Web Development Project",
        category: "Web Development",
        description: "Custom web application with modern architecture and scalable design",
        image: "/web.jpg",
        features: [
            { icon: "fa-code", text: "Clean Code" },
            { icon: "fa-layer-group", text: "Modular Design" }
        ]
    },
    {
        name: "Advanced Digital Solution",
        category: "Full Stack Development",
        description: "End-to-end web application with cutting-edge technologies",
        image: "/web2.jpg",
        features: [
            { icon: "fa-cogs", text: "Automation" },
            { icon: "fa-shield-alt", text: "Secure & Scalable" }
        ]
    }
];

const ProjectsSlider = () => {
    const sliderTrackRef = useRef(null);

    useEffect(() => {
        const sliderTrack = sliderTrackRef.current;
        if (!sliderTrack) return;

        const handleMouseEnter = () => {
            sliderTrack.style.animationPlayState = 'paused';
        };
        const handleMouseLeave = () => {
            sliderTrack.style.animationPlayState = 'running';
        };

        sliderTrack.addEventListener('mouseenter', handleMouseEnter);
        sliderTrack.addEventListener('mouseleave', handleMouseLeave);

        let startX = 0;
        let isDragging = false;
        let currentTranslateX = 0;

        const handleTouchStart = (e) => {
            startX = e.touches[0].clientX;
            isDragging = true;
            sliderTrack.style.animationPlayState = 'paused';

            const style = window.getComputedStyle(sliderTrack);
            const matrix = new WebKitCSSMatrix(style.transform);
            currentTranslateX = matrix.m41;
        };

        const handleTouchMove = (e) => {
            if (!isDragging) return;
            const currentX = e.touches[0].clientX;
            const diff = currentX - startX;
            const translateX = currentTranslateX + diff;
            sliderTrack.style.transform = `translateX(${translateX}px)`;
        };

        const handleTouchEnd = () => {
            if (!isDragging) return;
            isDragging = false;
            sliderTrack.style.animationPlayState = 'running';
        };

        sliderTrack.addEventListener('touchstart', handleTouchStart);
        sliderTrack.addEventListener('touchmove', handleTouchMove);
        sliderTrack.addEventListener('touchend', handleTouchEnd);

        return () => {
            sliderTrack.removeEventListener('mouseenter', handleMouseEnter);
            sliderTrack.removeEventListener('mouseleave', handleMouseLeave);
            sliderTrack.removeEventListener('touchstart', handleTouchStart);
            sliderTrack.removeEventListener('touchmove', handleTouchMove);
            sliderTrack.removeEventListener('touchend', handleTouchEnd);
        };
    }, []);

    return (
        <section id="projects" className="projects-slider-section">
            <div className="slider-container-fluid">
                <div className="slider-header">
                    <h2 className="slider-title">Real Projects. Real Growth.</h2>
                    <p className="slider-tagline">Every project tells a story of innovation and success</p>
                </div>

                <div className="slider-wrapper">
                    <button className="slider-btn prev" id="sliderPrev" aria-label="Previous slide">
                        <i className="fas fa-chevron-left"></i>
                    </button>

                    <div className="slider-viewport">
                        <div className="slider-track" id="sliderTrack" ref={sliderTrackRef}>
                            {/* Original Cards */}
                            {projects.map((project, index) => (
                                <div className="project-slide-card" key={`orig-${index}`}>
                                    <div className="card-inner">
                                        <div className="project-image-wrapper">
                                            <img src={project.image} alt={project.name} className="project-img" loading="lazy" />
                                            <div className="image-overlay"></div>
                                        </div>
                                        <div className="project-content">
                                            <span className="project-category">{project.category}</span>
                                            <h3 className="project-name">{project.name}</h3>
                                            <p className="project-desc">{project.description}</p>
                                            <div className="project-features">
                                                {project.features.map((feature, fIndex) => (
                                                    <span className="feature-badge" key={fIndex}>
                                                        <i className={`fas ${feature.icon}`}></i> {feature.text}
                                                    </span>
                                                ))}
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            ))}
                            {/* Duplicate Cards for Seamless Loop */}
                            {projects.map((project, index) => (
                                <div className="project-slide-card" key={`dup-${index}`}>
                                    <div className="card-inner">
                                        <div className="project-image-wrapper">
                                            <img src={project.image} alt={project.name} className="project-img" loading="lazy" />
                                            <div className="image-overlay"></div>
                                        </div>
                                        <div className="project-content">
                                            <span className="project-category">{project.category}</span>
                                            <h3 className="project-name">{project.name}</h3>
                                            <p className="project-desc">{project.description}</p>
                                            <div className="project-features">
                                                {project.features.map((feature, fIndex) => (
                                                    <span className="feature-badge" key={fIndex}>
                                                        <i className={`fas ${feature.icon}`}></i> {feature.text}
                                                    </span>
                                                ))}
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    <button className="slider-btn next" id="sliderNext" aria-label="Next slide">
                        <i className="fas fa-chevron-right"></i>
                    </button>
                </div>

                <div className="slider-indicators" id="sliderIndicators"></div>
            </div>
        </section>
    );
};

export default ProjectsSlider;
