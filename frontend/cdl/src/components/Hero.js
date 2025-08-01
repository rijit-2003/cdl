import React from 'react';
import './styles/Hero.css';

function HeroSection() {
  return (
    <div className="hero-section">
      <div className="hero-content">
        <h1 className="hero-title">Rediscover the Cosmic Distance Ladder</h1>
        <p className="hero-subtitle">“We have traveled this way before, and there is much to be learned by returning to our beginnings.”
– Carl Sagan, Cosmos</p>
        {/* <p className="hero-subtitle">“Equipped with his five senses, man explores the universe around him and calls the adventure Science.”
– Edwin Hubble</p> */}
      </div>
    </div>
  );
}

export default HeroSection;
