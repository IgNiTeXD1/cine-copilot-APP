import React, { useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const PageContainer = styled.div`
  padding: 40px;
  background: linear-gradient(135deg, #4b134f, #c94b4b);
  color: #FFFFFF;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Title = styled.h1`
  font-size: 36px;
  margin-bottom: 30px;
  color: #FFF;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.6);
`;

const Description = styled.p`
  font-size: 18px;
  text-align: center;
  max-width: 700px;
  margin-bottom: 40px;
  line-height: 1.6;
`;

const Button = styled.button`
  padding: 18px 40px;
  background-color: #8a2be2;
  border: none;
  border-radius: 10px;
  font-size: 20px;
  font-weight: bold;
  color: white;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 25px rgba(138, 43, 226, 0.65);
  }
`;

const FileInputContainer = styled.div`
  width: 70%;
  padding: 15px;
  margin: 20px 0;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  transition: box-shadow 0.3s ease;

  &:hover {
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
  }
`;

const FileInputLabel = styled.label`
  font-size: 16px;
  color: #333;
`;

const FileInput = styled.input`
  display: none;
`;

const FileNameDisplay = styled.span`
  font-size: 14px;
  color: #666;
  margin-left: 10px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
`;

const ShotClassification = () => {
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
      const response = await axios.post('http://localhost:8080/shot', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      navigate('/shot-results', { state: { shotDetails: response.data.shot_details }});
    } catch (error) {
      console.error('Error uploading the file:', error);
      alert('Upload failed!');
    }
  };

  return (
    <PageContainer>
      <Title>Shot Classification</Title>
      <Description>
        Upload your video and our system will analyze the footage to classify different camera shots. Understand how various shot types are used throughout your video to enhance storytelling.
      </Description>
      <FileInputContainer onClick={() => document.getElementById('fileInput').click()}>
        <FileInputLabel>Click to select a file</FileInputLabel>
        <FileInput id="fileInput" type="file" onChange={handleFileChange} accept="video/*" />
        <FileNameDisplay>{file ? file.name : 'No file selected'}</FileNameDisplay>
      </FileInputContainer>
      <Button onClick={handleUpload}>Analyze Shots</Button>
    </PageContainer>
  );
};

export default ShotClassification;




