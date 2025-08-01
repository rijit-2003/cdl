import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Home from './pages/Home';
import ScientistDetail from './pages/ScientistDetail'; // ✅ Already imported

import Particles from 'react-tsparticles';
import { loadStarsPreset } from 'tsparticles-preset-stars'; // ✅ Correct preset

function App() {
  const particlesInit = async (engine) => {
    await loadStarsPreset(engine);
  };

  return (
    <Router>
      <div className="App">
        {/* Starry Background */}
        <Particles
          id="tsparticles"
          init={particlesInit}
          options={{
            preset: 'stars',
            fullScreen: {
              enable: true,
              zIndex: -1,
            },
          }}
        />

        <Navbar />
        <Hero />

        <div className="app-container">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/scientist/:id" element={<ScientistDetail />} /> {/* ✅ New Route */}
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
