import React, { useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const PageContainer = styled.div`
  padding: 20px;
  background: linear-gradient(to right, #008080, #70a1ff);  // Teal to light blue gradient
  color: #F0F0F0;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Title = styled.h1`
  font-size: 28px;
  margin-bottom: 20px;
  color: #FFFFFF;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
`;

const Description = styled.p`
  font-size: 16px;
  text-align: center;
  max-width: 600px;
  margin-bottom: 30px;
  line-height: 1.5;
  font-family: 'Arial', sans-serif;
`;

const Button = styled.button`
  padding: 15px 30px;
  background-color: #00ced1;
  border: none;
  border-radius: 8px;
  font-size: 18px;
  color: white;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 20px rgba(0, 206, 209, 0.5);
  }
`;

const FileInputContainer = styled.div`
  width: 60%;
  background: #e0f0f0;
  padding: 12px 20px;
  margin: 20px 0;
  border-radius: 5px;
  border: 2px solid #007bff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  transition: background-color 0.3s ease, border-color 0.3s ease;

  &:hover {
    background-color: #b0e0e6;  // Light blue hover background
    border-color: #00ced1;  // Dark turquoise hover border
  }
`;

const FileInputLabel = styled.label`
  color: #333;
  font-size: 16px;
  flex-grow: 1;
`;

const FileNameDisplay = styled.span`
  color: #555;
  font-size: 14px;
  margin-left: 10px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
`;

const FileInput = styled.input`
  display: none;
`;

const VideoSegregation = () => {
  const [file, setFile] = useState(null);
  const navigate = useNavigate();

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8080/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      navigate('/video-results', { state: { downloadLinks: response.data.download_links }});
    } catch (error) {
      console.error('Error uploading the file:', error);
      alert('Upload failed!');
    }
  };

  return (
    <PageContainer>
      <Title>Video Segregation</Title>
      <Description>
        Our tool automatically detects and categorizes scene changes using advanced vision algorithms. Whether it's a cut, dissolve, fade, or wipe, our system accurately segments videos based on transitions, making it easier for editors and filmmakers to analyze scene structure.
      </Description>
      <FileInputContainer onClick={() => document.getElementById('fileInput').click()}>
        <FileInputLabel htmlFor="fileInput">Click to select a file</FileInputLabel>
        <FileInput id="fileInput" type="file" onChange={handleFileChange} accept="video/*" />
        <FileNameDisplay>{file ? file.name : 'No file selected'}</FileNameDisplay>
      </FileInputContainer>
      <Button onClick={handleUpload}>Import Video</Button>
    </PageContainer>
  );
};

export default VideoSegregation;


