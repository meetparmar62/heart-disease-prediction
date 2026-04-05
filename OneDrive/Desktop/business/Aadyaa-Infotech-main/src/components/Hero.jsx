import React, { useEffect } from 'react';

const Hero = () => {
    useEffect(() => {
        const isMobile = window.innerWidth <= 768;
        if (!isMobile) {
            const particles = document.querySelectorAll('.particle');

            particles.forEach((particle, index) => {
                let angle = Math.random() * Math.PI * 2;
                let speed = 0.001 + Math.random() * 0.002;
                let radius = 50 + Math.random() * 50;

                function animateParticle() {
                    angle += speed;
                    const x = Math.cos(angle) * radius;
                    const y = Math.sin(angle) * radius;

                    particle.style.transform = `translate(${x}px, ${y}px)`;
                    requestAnimationFrame(animateParticle);
                }

                animateParticle();
            });

            const handleMouseMove = (e) => {
                const x = (e.clientX / window.innerWidth - 0.5) * 20;
                const y = (e.clientY / window.innerHeight - 0.5) * 20;

                const particlesList = document.querySelectorAll('.particle');
                particlesList.forEach((particle, index) => {
                    const speed = (index + 1) * 0.5;
                    particle.style.transform = `translate(${x * speed}px, ${y * speed}px)`;
                });
            };

            const heroSection = document.querySelector('.hero');
            if (heroSection) {
                heroSection.addEventListener('mousemove', handleMouseMove);
            }

            const handleScroll = () => {
                const scrolled = window.pageYOffset;
                const heroBackground = document.querySelector('.hero-background');
                if (heroBackground) {
                    heroBackground.style.transform = `translateY(${scrolled * 0.5}px)`;
                }
            };
            window.addEventListener('scroll', handleScroll);

            return () => {
                if (heroSection) heroSection.removeEventListener('mousemove', handleMouseMove);
                window.removeEventListener('scroll', handleScroll);
            };
        }
    }, []);

    return (
        <section id="home" className="hero">
            <div className="hero-background">
                <div className="particle" id="particle1"></div>
                <div className="particle" id="particle2"></div>
                <div className="particle" id="particle3"></div>
            </div>
            <div className="hero-content">
                <div className="left fade-in">
                    <div className="content-wrapper">
                    </div>
                </div>

                <div className="right fade-in delay-2">
                </div>
            </div>
        </section>
    );
};

export default Hero;
