import React from 'react';

const industries = [
    { name: "Education & EdTech", image: "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=400&h=300&fit=crop" },
    { name: "Real Estate", image: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=400&h=300&fit=crop" },
    { name: "Manufacturing", image: "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&h=300&fit=crop" },
    { name: "Food & Beverage", image: "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400&h=300&fit=crop" },
    { name: "Travel & Hospitality", image: "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=400&h=300&fit=crop" },
    { name: "Healthcare", image: "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400&h=300&fit=crop" },
    { name: "Finance & Banking", image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop" },
    { name: "E-commerce & Retail", image: "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=400&h=300&fit=crop" },
    { name: "Logistics & Supply Chain", image: "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=400&h=300&fit=crop" },
    { name: "Media & Entertainment", image: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=400&h=300&fit=crop" },
    { name: "Energy & Utilities", image: "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=400&h=300&fit=crop" },
    { name: "SaaS & Technology", image: "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=400&h=300&fit=crop" },
    { name: "Legal & Compliance", image: "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400&h=300&fit=crop" },
    { name: "Automotive", image: "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400&h=300&fit=crop" },
    { name: "Agriculture & Agritech", image: "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?w=400&h=300&fit=crop" },
    { name: "Construction", image: "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=400&h=300&fit=crop" },
    { name: "Fitness & Wellness", image: "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=300&fit=crop" },
    { name: "Event Management", image: "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=400&h=300&fit=crop" },
    { name: "Beauty & Personal Care", image: "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=400&h=300&fit=crop" },
    { name: "Gaming & Esports", image: "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400&h=300&fit=crop" }
];

const Industries = () => {
    return (
        <section className="industries-section">
            <div className="container">
                <div className="industries-header">
                    <span className="section-label">INDUSTRIES WE SERVE</span>
                    <h2 className="section-title">Solutions Built for Every Industry</h2>
                    <p className="section-description">From healthcare to hospitality, we deliver tailored digital solutions that drive growth and innovation across diverse sectors worldwide.</p>
                </div>

                <div className="industries-grid" id="industriesGrid">
                    {/* Map all industries */}
                    {industries.map((industry, index) => (
                        <div className="industry-card" key={`ind-${index}`}>
                            <img src={industry.image} alt={industry.name} className="industry-image" />
                            <h3 className="industry-name">{industry.name}</h3>
                        </div>
                    ))}
                    {/* Duplicate mapping for seamless loop if needed, but the original seems to have them for a marquee effect */}
                    {industries.map((industry, index) => (
                        <div className="industry-card" key={`dup-${index}`}>
                            <img src={industry.image} alt={industry.name} className="industry-image" />
                            <h3 className="industry-name">{industry.name}</h3>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default Industries;
