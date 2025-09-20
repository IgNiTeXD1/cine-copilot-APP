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
- **Libraries**: OpenCV, PyTorch, TensorFlow, Pandas, FAISS  
- **Models**: MobileNetV2, ResNet-18, CNNs, Optical Flow  
- **Deployment**: Modular APIs, Web-based interface  

---

## 📦 Installation

### 1. Clone the Repository

git clone https://github.com/yourusername/cinecopilot.git
cd cinecopilot
2. Create Virtual Environment & Install Dependencies
bash
Copy code
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
3. Start Backend (FastAPI)
bash
Copy code
uvicorn app.main:app --reload
4. Start Frontend (React)
bash
Copy code
cd frontend
npm install
npm start
🚀 Usage
Open the web dashboard in your browser.

Upload a video file.

Choose the analysis module:

Scene Segmentation

Shot & Camera Angle Classification

Lighting Analysis

Character Binning

View results in interactive charts or download CSV reports.

📊 Example Outputs
Shot Transition CSV → Frame-wise boundaries of cuts & transitions.

Camera Angle Heatmap → Distribution of shots (close-up, wide, OTS, etc.).

Lighting Report → Brightness, contrast, shadow intensity, glare presence.

Character Video Clips → Extracted segments of a chosen character.
