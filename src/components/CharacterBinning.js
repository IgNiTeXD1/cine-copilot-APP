import React, { useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const PageContainer = styled.div`
  padding: 40px;
  background: linear-gradient(135deg, rgb(233, 206, 0), rgb(242, 244, 193));
  color: rgb(255, 255, 255);
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Title = styled.h1`
  font-size: 48px;
  margin-bottom: 30px;
  color: #FFF;
`;

const Description = styled.p`
  font-size: 18px;
  text-align: center;
  max-width: 800px;
  margin-bottom: 40px;
  line-height: 1.6;
`;

const Button = styled.button`
  padding: 18px 40px;
  background-color: rgb(134, 87, 0);
  border: none;
  border-radius: 10px;
  font-size: 20px;
  font-weight: bold;
  color: white;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 25px rgba(134, 87, 0, 0.65);
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
  color: #4B0082;
`;

const FileNameDisplay = styled.span`
  font-size: 14px;
  color: #666;
  margin-left: 10px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
`;

const FileInput = styled.input`
  display: none;
`;

const CharacterBinning = () => {
  const navigate = useNavigate();
  const [videoFile, setVideoFile] = useState(null);
  const [imageFiles, setImageFiles] = useState([]);

  const handleVideoChange = (event) => {
    setVideoFile(event.target.files[0]);
  };

  const handleImagesChange = (event) => {
    setImageFiles([...event.target.files]);
  };

  const handleVideoUpload = async () => {
    if (!videoFile) {
      alert('Please select a video file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', videoFile);

    try {
      const response = await axios.post('http://localhost:8080/upload_video', formData);
      navigate('/shot-results', { state: { shotDetails: response.data.shot_details }});
    } catch (error) {
      console.error('Error uploading the video:', error);
      alert('Upload failed!');
    }
  };

  const handleImagesUpload = async () => {
    if (imageFiles.length === 0) {
      alert('Please select images before submitting!');
      return;
    }
    const formData = new FormData();
    imageFiles.forEach((file) => formData.append('images', file));

    try {
      const response = await axios.post('http://localhost:8080/upload_images', formData);
      console.log('Images uploaded successfully', response.data);
    } catch (error) {
      console.error('Error uploading the images:', error);
    }
  };

  const downloadVideo = async () => {
    const videoUrl = `http://localhost:8080/download_video?video_name=output_video.mp4`;
    const response = await axios.get(videoUrl, { responseType: 'blob' });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'output_video.mp4'); // You can specify a different name
    document.body.appendChild(link);
    link.click();
    link.parentNode.removeChild(link);
  };

  return (
    <PageContainer>
      <Title>Character Binning</Title>
      <Description>
        Upload your video and images. Our system will analyze the footage to classify the uploaded reference images.
      </Description>
      <FileInputContainer onClick={() => document.getElementById('videoInput').click()}>
        <FileInputLabel htmlFor="videoInput">Select Video</FileInputLabel>
        <FileInput id="videoInput" type="file" onChange={handleVideoChange} accept="video/*" />
        <FileNameDisplay>{videoFile ? videoFile.name : 'No video selected'}</FileNameDisplay>
      </FileInputContainer>
      <Button onClick={handleVideoUpload}>Analyze Video Shots</Button>
      <p>Upload images here</p>
      <FileInputContainer onClick={() => document.getElementById('imageInput').click()}>
        <FileInputLabel htmlFor="imageInput">Select Images</FileInputLabel>
        <FileInput id="imageInput" type="file" onChange={handleImagesChange} accept="image/*" multiple />
        <FileNameDisplay>{imageFiles.length > 0 ? `${imageFiles.length} files selected` : 'No images selected'}</FileNameDisplay>
      </FileInputContainer>
      <Button onClick={handleImagesUpload}>Analyze Images</Button>
      <Button onClick={downloadVideo}>Download Processed Video</Button>
    </PageContainer>
  );
};

export default CharacterBinning;



