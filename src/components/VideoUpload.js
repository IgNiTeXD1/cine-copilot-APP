import React, { useState } from 'react';
import axios from 'axios';

const VideoUpload = () => {
    const [file, setFile] = useState(null); // State to hold the file

    const handleFileChange = (event) => {
        setFile(event.target.files[0]); // Update state when file is selected
    };

    const handleUpload = async () => {
        if (!file) {
            alert('Please select a file first!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:8080/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log('Server response:', response.data);
        } catch (error) {
            console.error('Error uploading the file:', error);
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} accept="video/*" />
            <button onClick={handleUpload}>Upload Video</button>
        </div>
    );
};

export default VideoUpload;

