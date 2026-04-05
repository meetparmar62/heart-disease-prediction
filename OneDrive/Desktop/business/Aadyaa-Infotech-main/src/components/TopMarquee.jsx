import React from 'react';

const TopMarquee = () => {
    const text = "SPECIAL OFFER • AADYAA INFOTECH • LIMITED PERIOD DEAL • ";
    return (
        <div className="top-marquee-bar">
            <div className="marquee-inner">
                {[...Array(10)].map((_, i) => (
                    <span key={i}>{text}</span>
                ))}
            </div>
        </div>
    );
};

export default TopMarquee;
