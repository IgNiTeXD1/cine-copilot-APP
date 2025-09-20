import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AppHeader from './components/AppHeader';
import HomePage from './components/HomePage';
import FeaturesGrid from './components/FeaturesGrid';
import VideoSegregation from './components/VideoSegregation';
import ShotClassification from './components/ShotClassification';
import CameraAngleClassification from './components/CameraAngleClassification';
import LightComposition from './components/LightComposition';
import CharacterBinning from './components/CharacterBinning'; // Ensure this component is created
import VideoUpload from './components/VideoUpload';
import VideoResults from './components/VideoResults';

function App() {
  return (
    <Router>
      <AppHeader />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/features" element={<FeaturesGrid />} />
        <Route path="/video-segregation" element={<VideoSegregation />} />
        <Route path="/shot-classification" element={<ShotClassification />} />
        <Route path="/camera-angle-classification" element={<CameraAngleClassification />} />
        <Route path="/light-composition" element={<LightComposition />} />
        <Route path="/character-binning" element={<CharacterBinning />} />
        <Route path="/upload-video" element={<VideoUpload />} />
        <Route path="/video-results" element={<VideoResults />} />
      </Routes>
    </Router>
  );
}

export default App;






