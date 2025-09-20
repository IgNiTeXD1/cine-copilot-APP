# 🎬 CineCopilot – AI-Powered Video Segmentation & Cinematographic Analysis  

CineCopilot is an **AI-driven video analysis toolkit** that automates scene segmentation, shot classification, camera angle detection, lighting analysis, and character binning.  
It is designed for **filmmakers, editors, students, and researchers** who want structured insights into cinematographic storytelling without tedious manual work.  

---

## ✨ Features
- 🎥 **Scene Segmentation** – Detects hard cuts, fades, dissolves using **SSIM**, histogram analysis, and optical flow.  
- 📸 **Shot & Camera Angle Classification** – Classifies shot sizes (close-up, medium, wide) and camera angles (eye-level, high, low, Dutch tilt) using **ResNet-18 & CNNs**.  
- 🧑‍🤝‍🧑 **Character Binning** – Groups video frames by characters using **MobileNetV2 embeddings + cosine similarity**.  
- 💡 **Lighting Analysis** – Evaluates brightness, contrast, color temperature, glare, and shadows with structured reports.  
- 🌐 **Web Dashboard** – React + FastAPI interface for uploading videos, running analysis, and visualizing results.  
- 📊 **Export & Reports** – Scene-wise CSVs, heatmaps, radar charts, and extracted video clips for insights.  

---

## 🛠️ Tech Stack
- **Frontend**: React  
- **Backend**: FastAPI, Redis  
- **Libraries**: OpenCV, PyTorch, TensorFlow, Pandas, FAISS ,SSIM 
- **Models**: MobileNetV2, ResNet-18, CNNs, Optical Flow  

SSIM SEGMETATION:
<img width="873" height="361" alt="image" src="https://github.com/user-attachments/assets/ff2f032b-6ffe-455a-954b-a04c7678e1a0" />

LIGHT COMP ANALYTICS:
<img width="940" height="449" alt="image" src="https://github.com/user-attachments/assets/f52357b8-42ca-4ebe-b842-e144d8b49aae" />
<img width="940" height="450" alt="image" src="https://github.com/user-attachments/assets/487909b2-dbd6-4ff4-b0f1-9662d1087b77" />

CAMERA ANGLE COMPOSITION ANALYTICS:
<img width="940" height="433" alt="image" 
  src="https://github.com/user-attachments/assets/37afa7e0-30f8-425e-b5db-aff7c5c88292" />
  <img width="940" height="433" alt="image" src="https://github.com/user-attachments/assets/91095cef-094c-45b3-987d-0450415907df" />






