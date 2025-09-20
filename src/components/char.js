// import React, { useState } from 'react';
// import styled from 'styled-components';
// import { useNavigate } from 'react-router-dom';
// import axios from 'axios';

// const PageContainer = styled.div`
//   padding: 40px;
//   background-color: #0051ff;
//   color: #FFFFFF;
//   height: 100vh;
//   display: flex;
//   flex-direction: column;
//   align-items: center;
//   justify-content: center;
// `;

// const Title = styled.h1`
//   font-size: 48px;
//   margin-bottom: 20px;
//   font-weight: bold;
// `;

// const Description = styled.p`
//   font-size: 18px;
//   text-align: center;
//   max-width: 800px;
//   margin-bottom: 30px;
//   line-height: 1.6;
// `;

// const Button = styled.button`
//   padding: 15px 35px;
//   background-color: rgb(0, 13, 114);
//   border: none;
//   border-radius: 8px;
//   font-size: 20px;
//   font-weight: bold;
//   color: #000;
//   cursor: pointer;
//   transition: transform 0.3s ease, box-shadow 0.3s ease;

//   &:hover {
//     transform: scale(1.05);
//     box-shadow: 0 2px 15px rgba(224, 220, 247, 0.6);
//   }
// `;

// const FileInput = styled.input`
//   margin: 10px;
// `;

// const CharacterBinning = () => {
//   const navigate = useNavigate();
//   const [videoFile, setVideoFile] = useState(null);
//   const [imageFiles, setImageFiles] = useState([]);

//   const handleVideoChange = (event) => {
//     setVideoFile(event.target.files[0]); // Only one video can be selected
//   };

//   const handleImagesChange = (event) => {
//     if (event.target.files.length > 10) {
//       alert('You can only upload up to 10 images.');
//       return;
//     }
//     setImageFiles([...event.target.files]);
//   };

//   // const handleVideoUpload = async () => {
//   //   if (!videoFile) {
//   //     alert('Please select a video before submitting!');
//   //     return;
//   //   }
//   //   const formData = new FormData();
//   //   formData.append('video', videoFile);
    
//   //   try {
//   //     const response = await axios.post('http://localhost:8000/upload_video', formData, {
//   //       headers: {
//   //         'Content-Type': 'multipart/form-data',
//   //       },
//   //     });
//   //     console.log('Video uploaded successfully', response.data);
//   //   } catch (error) {
//   //     console.error('Error uploading the video:', error);
//   //     alert('Video upload failed!');
//   //   }
//   // };

//   const handleUpload = async () => {
//     if (!videoFile) {
//       alert('Please select a file first!');
//       return;
//     }

//     const formData = new FormData();
//     formData.append('file', videoFile);

//     try {
//       const response = await axios.post('http://localhost:8000/upload_video', formData, {
//         headers: {
//           'Content-Type': 'multipart/form-data',
//         },
//       });
//       navigate('/video-results', { state: { downloadLinks: response.data.download_links }});
//     } catch (error) {
//       console.error('Error uploading the file:', error);
//       alert('Upload failed!');
//     }
//   };
//   const handleImagesUpload = async () => {
//     if (imageFiles.length === 0) {
//       alert('Please select images before submitting!');
//       return;
//     }
//     const formData = new FormData();
//     imageFiles.forEach((file) => formData.append('images', file));
    
//     try {
//       const response = await axios.post('http://localhost:8000/upload_images', formData, {
//         headers: {
//           'Content-Type': 'multipart/form-data',
//         },
//       });
//       console.log('Images uploaded successfully', response.data);
//     } catch (error) {
//       console.error('Error uploading the images:', error);
//       alert('Image upload failed!');
//     }
//   };

//   return (
//     <PageContainer>
//       <Title>Character Binning Analysis</Title>
//       <Description>
//         Character Binning helps in understanding character distribution and frequency across your media files. It uses advanced algorithms to categorize characters based on their appearance and actions, providing insights into character development and screen presence.
//       </Description>
//       <p>Upload video here</p>
//       <FileInput type="file" accept="video/*" onChange={handleVideoChange} />
//       <Button onClick={handleUpload}>Upload Video</Button>
//       <p>Upload images here</p>
//       <FileInput type="file" accept="image/*" multiple onChange={handleImagesChange} />
//       <Button onClick={handleImagesUpload}>Upload Images</Button>
//     </PageContainer>
//   );
// }

// export default CharacterBinning;