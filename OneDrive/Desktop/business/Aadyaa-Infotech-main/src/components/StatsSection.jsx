import React from 'react';

const StatsSection = () => {
    return (
        <section className="stats-section">
            <div className="stats-container">
                <div className="stat-item">
                    <div className="stat-icon">
                        <i className="fas fa-project-diagram"></i>
                    </div>
                    <div className="stat-number">100+</div>
                    <div className="stat-label">Dynamic Projects Done</div>
                </div>

                <div className="stat-item">
                    <div className="stat-icon">
                        <i className="fas fa-smile"></i>
                    </div>
                    <div className="stat-number">95+</div>
                    <div className="stat-label">Happy Clients</div>
                </div>

                <div className="stat-item">
                    <div className="stat-icon">
                        <i className="fas fa-clock"></i>
                    </div>
                    <div className="stat-number">8+</div>
                    <div className="stat-label">Years Experience</div>
                </div>

                <div className="stat-item">
                    <div className="stat-icon">
                        <i className="fas fa-headset"></i>
                    </div>
                    <div className="stat-number">24/7</div>
                    <div className="stat-label">Support</div>
                </div>
            </div>
        </section>
    );
};

export default StatsSection;
