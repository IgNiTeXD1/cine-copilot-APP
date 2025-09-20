import React from 'react';
import { useLocation } from 'react-router-dom';
import styled from 'styled-components';

const ResultsContainer = styled.div`
  padding: 20px;
  background-color: #1A1A1A;
  color: white;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Title = styled.h1`
  font-size: 24px;
  color: #FFF;
`;

const DownloadLink = styled.a`
  margin: 10px;
  color: #FFA500;
  cursor: pointer;
  text-decoration: none;

  &:hover {
    color: #FFD700;
  }
`;

const VideoResults = () => {
  const location = useLocation();
  const { downloadLinks } = location.state || { downloadLinks: [] };

  return (
    <ResultsContainer>
      <Title>Processed Video Segments</Title>
      {downloadLinks.length > 0 ? (
        downloadLinks.map((link, index) => (
          <DownloadLink key={index} href={link} download>Download Segment {index + 1}</DownloadLink>
        ))
      ) : (
        <p>No video segments to display.</p>
      )}
    </ResultsContainer>
  );
};

export default VideoResults;

