import React from 'react';

const ProcessSection = () => {
    const steps = [
        {
            icon: "fa-comments",
            title: "Free Consultation",
            desc: "We discuss your requirements, goals, and budget to understand your vision"
        },
        {
            icon: "fa-clipboard-list",
            title: "Strategy & Planning",
            desc: "Our team creates a detailed roadmap with timeline and cost estimate"
        },
        {
            icon: "fa-code",
            title: "Development & Testing",
            desc: "We build your solution with regular updates and thorough testing"
        },
        {
            icon: "fa-rocket",
            title: "Launch & Support",
            desc: "Go live with your project and get 24/7 ongoing support"
        }
    ];

    return (
        <section className="process-section">
            <div className="container">
                <h2 className="section-title">How We Work</h2>
                <p className="section-subtitle">Simple 4-step process to bring your ideas to life</p>

                <div className="process-timeline">
                    {steps.map((step, index) => (
                        <div className="process-step" key={index}>
                            <div className="step-number">{index + 1}</div>
                            <div className="step-icon-wrapper">
                                <i className={`fas ${step.icon}`}></i>
                            </div>
                            <h3>{step.title}</h3>
                            <p>{step.desc}</p>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default ProcessSection;
