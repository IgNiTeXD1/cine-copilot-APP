import React from 'react';
import styled, { keyframes } from 'styled-components';
import { Link } from 'react-router-dom';

// Smooth animations for text
const fadeInUp = keyframes`
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
`;

const pulse = keyframes`
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
`;

const textFocusIn = keyframes`
  from {
    filter: blur(12px);
    opacity: 0;
  }
  to {
    filter: blur(0px);
    opacity: 1;
  }
`;

// Styled components with enhanced design
const HomePageContainer = styled.div`
  color: #333;
  background: linear-gradient(120deg, #e0eafc, #cfdef3);
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0 20px;
  overflow: hidden;
`;

const Header = styled.header`
  background: transparent;
  width: 100%;
  padding: 20px 0;
  text-align: center;
`;

const Title = styled.h1`
  font-size: 4rem;
  color: #224;
  margin: 0;
  font-weight: 900;
  animation: ${pulse} 3s infinite ease-in-out;
`;

const Tagline = styled.p`
  font-size: 1.5rem;
  color: #444;
  margin-top: 20px;
  animation: ${textFocusIn} 3s ease-out forwards;
`;

const FeaturesList = styled.ul`
  list-style: none;
  padding: 0;
  margin-top: 30px;
  text-align: center;
`;

const FeatureItem = styled.li`
  font-size: 1.25rem;
  margin-bottom: 20px;
  color: #555;
  animation: ${fadeInUp} 2s ease-out forwards;
`;

const ExploreButton = styled(Link)`
  color: #5C6BC0;
  background: transparent;
  border: 2px solid #5C6BC0;
  padding: 12px 24px;
  border-radius: 5px;
  font-size: 1.1rem;
  font-weight: bold;
  text-decoration: none;
  transition: all 0.3s ease;

  &:hover {
    background-color: #5C6BC0;
    color: white;
    box-shadow: 0 3px 20px rgba(0,0,0,0.3);
  }
`;

// HomePage component
const HomePage = () => (
  <HomePageContainer>
    <Header>
      <Title>CINE-COPILOT</Title>
    </Header>
    <Tagline>Start exploring your videos like never before!</Tagline>
    <FeaturesList>
      <FeatureItem>🎬 Segregates videos based on transitions.</FeatureItem>
      <FeatureItem>📐 Classifies camera angles & shots.</FeatureItem>
      <FeatureItem>💡 Provides a lighting report.</FeatureItem>
      <FeatureItem>🎥 Delivers key cinematic insights.</FeatureItem>
    </FeaturesList>
    <ExploreButton to="/features">Explore More</ExploreButton>
  </HomePageContainer>
);

export default HomePage;
 



