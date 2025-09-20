import React from 'react';
import styled, { keyframes } from 'styled-components';
import { Link } from 'react-router-dom';
import lightCompositionImage from 'C:\\Users\\91735\\cine-copilot-app - Copy\\src\\images\\image.jpg';
import shotscale from 'C:\\Users\\91735\\cine-copilot-app - Copy\\src\\images\\arival.jpg';
import videoseg from 'C:\\Users\\91735\\cine-copilot-app - Copy\\src\\images\\dune.jpg';
import charbinn from 'C:\\Users\\91735\\cine-copilot-app - Copy\\src\\images\\space.jpg';
import cameraang from 'C:\\Users\\91735\\cine-copilot-app - Copy\\src\\images\\test.jpg';


// Animation for page content
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

// Define styled components
const GridContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr); // Adjust if needed to fit all cards comfortably
  gap: 40px;
  padding: 40px;
  background: #f0f0f0;
`;

const Card = styled.div`
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  transition: transform 0.3s ease-in-out, box-shadow 0.5s ease-in-out;
  cursor: pointer;
  animation: ${fadeInUp} 0.8s ease-out;

  &:hover {
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 15px 30px rgba(0,0,0,0.3);
  }
`;

const CardImage = styled.img`
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
`;

const CardContent = styled.div`
  padding: 20px;
`;

const CardTitle = styled.h3`
  font-size: 20px;
  color: #333;
  margin-bottom: 5px;
`;



const StyledLink = styled(Link)`
  text-decoration: none;
  color: inherit;
`;

// FeaturesGrid component with images and animations
const FeaturesGrid = () => {
  return (
    <GridContainer>
      <Card>
        <StyledLink to="/video-segregation">
          <CardImage src={videoseg} alt="Video Segregation" />
          <CardContent>
            <CardTitle>Video Segregation</CardTitle>
           
          </CardContent>
        </StyledLink>
      </Card>
      <Card>
        <StyledLink to="/shot-classification">
          <CardImage src={shotscale} alt="Shot Classification" />
          <CardContent>
            <CardTitle>Shot Classification</CardTitle>
            
          </CardContent>
        </StyledLink>
      </Card>
      <Card>
        <StyledLink to="/camera-angle-classification">
          <CardImage src={cameraang} alt="Camera Angle Classification" />
          <CardContent>
            <CardTitle>Camera Angle Classification</CardTitle>
            
          </CardContent>
        </StyledLink>
      </Card>
      <Card>
        <StyledLink to="/light-composition">
          <CardImage src={lightCompositionImage} alt="Light Composition" />
          <CardContent>
            <CardTitle>Light Composition</CardTitle>
           
          </CardContent>
        </StyledLink>
      </Card>
      <Card>
        <StyledLink to="/character-binning">
          <CardImage src={charbinn} alt="Character Binning" />
          <CardContent>
            <CardTitle>Character Binning</CardTitle>
           
          </CardContent>
        </StyledLink>
      </Card>
    </GridContainer>
  );
};

export default FeaturesGrid;





