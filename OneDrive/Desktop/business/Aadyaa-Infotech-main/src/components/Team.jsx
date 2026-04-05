import React from 'react';

const teamStats = [
    { 
        value: "8+",
        label: "Years Experience",
        title: "Expert Developers", 
        subtitle: "Website & App Development",
        icon: "fa-code"
    },
    { 
        value: "6+",
        label: "Years Experience",
        title: "Creative Designer", 
        subtitle: "UI/UX & Graphics Design",
        icon: "fa-palette"
    },
    { 
        value: "4+",
        label: "Years Experience",
        title: "Business Strategy", 
        subtitle: "Growth & Strategic Planning",
        icon: "fa-chart-line"
    }
];

const Team = () => {
    return (
        <section id="team" className="excellence-section">
            <div className="container">
                <div className="excellence-header">
                    <div className="excellence-badge">
                        <span className="badge-dot"></span>
                        <i className="fas fa-award"></i>
                        <span>Proven Track Record</span>
                    </div>
                    
                    <h2 className="section-title">
                        Years of <span className="gradient-accent">Excellence</span>
                    </h2>
                    <p className="section-subtitle">Delivering exceptional results through expertise and innovation</p>
                    <div className="title-line"></div>
                </div>

                <div className="marquee-background">
                    <div className="marquee-inner">
                        <span>SPECIAL OFFER • AADYAA INFOTECH • LIMITED PERIOD DEAL • </span>
                        <span>SPECIAL OFFER • AADYAA INFOTECH • LIMITED PERIOD DEAL • </span>
                        <span>SPECIAL OFFER • AADYAA INFOTECH • LIMITED PERIOD DEAL • </span>
                        <span>SPECIAL OFFER • AADYAA INFOTECH • LIMITED PERIOD DEAL • </span>
                    </div>
                </div>

                <div className="excellence-grid">
                    {teamStats.map((stat, index) => (
                        <div className="excellence-card" key={index}>
                            <div className="icon-box">
                                <i className={`fas ${stat.icon}`}></i>
                            </div>
                            <h2 className="card-value">{stat.value}</h2>
                            <p className="card-label">{stat.label}</p>
                            <h3 className="card-title">{stat.title}</h3>
                            <p className="card-subtitle">{stat.subtitle}</p>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default Team;
