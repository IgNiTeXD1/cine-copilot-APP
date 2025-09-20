from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import cv2
from skimage.metrics import structural_similarity as compare_ssim
from werkzeug.utils import secure_filename
from uuid import uuid4
import subprocess  # Used for calling FFmpeg directly

app = FastAPI()

# Directory setup
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


FFMPEG_PATH = r'C:\Users\91735\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe'

def cut_video_on_transitions(input_video_path, output_folder, transition_threshold=0.4, min_scene_length=24):
    video = cv2.VideoCapture(input_video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    scenes = []
    prev_frame = None
    scene_number = 0
    scene_start_time = 0

    for frame_number in range(frame_count):
        ret, curr_frame = video.read()
        if not ret:
            break
        if prev_frame is not None:
            curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
            prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
            score, diff = compare_ssim(prev_gray, curr_gray, full=True)
            if score < transition_threshold:
                scene_end_time = frame_number / fps
                if scene_end_time - scene_start_time >= min_scene_length / fps:
                    output_filename = f"scene_{scene_number}.mp4"
                    output_path = os.path.join(output_folder, output_filename)
                    command = [
                        FFMPEG_PATH, 
                        '-ss', str(scene_start_time), 
                        '-to', str(scene_end_time),
                        '-i', input_video_path, 
                        '-c:v', 'copy',  # Copy the video stream
                        '-c:a', 'copy',  # Copy the audio stream
                        output_path
                    ]
                    try:
                        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        scenes.append(output_path)
                        scene_number += 1
                        scene_start_time = scene_end_time
                    except subprocess.CalledProcessError as e:
                        print(f"Error processing scene {scene_number}: {e.stderr}")
        prev_frame = curr_frame

    # Handle the last scene
    if scene_start_time < frame_count / fps:
        output_filename = f"scene_{scene_number}.mp4"
        output_path = os.path.join(output_folder, output_filename)
        command = [FFMPEG_PATH, '-ss', str(scene_start_time), '-i', input_video_path, '-c', 'copy', output_path]
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        scenes.append(output_path)

    video.release()
    return scenes


@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    if not file.filename.endswith('.mp4'):
        raise HTTPException(status_code=400, detail="Unsupported file format.")
    
    filename = secure_filename(file.filename)
    input_video_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(input_video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_paths = cut_video_on_transitions(input_video_path, OUTPUT_FOLDER)
    os.remove(input_video_path)

    return {"download_links": [f"/output/{os.path.basename(path)}" for path in output_paths]}

@app.get("/output/{filename}")
async def serve_clip(filename: str):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type='application/octet-stream')



