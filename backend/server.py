from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from video_processor import cut_video_on_transitions
from light import light
from cameralevelang import camer11
from sho import shot
from pathlib import Path
from smartsearchfinal import smart
from typing import List

# Constants for directory paths
UPLOAD_DIR = 'uploads'
OUTPUT_DIR = 'output'
UPLOAD_pho = 'upo_img'

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs('upo_img', exist_ok=True)

# Initialize FastAPI app
app = FastAPI()
light_obj = light()
cam_obj = camer11()
shot_obj = shot()
smart_obj = smart()
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify the client origins or use ["*"] for open access
    allow_credentials=True,
    allow_methods=["*"],  # You can customize this to ['GET', 'POST'] etc. as needed
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    if file.filename.endswith('.mp4'):  # Ensure it is a video file
        save_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Process the video
        output_files = cut_video_on_transitions(save_path, OUTPUT_DIR)

        # Cleanup the original upload
        os.remove(save_path)

        # Generate download links
        download_links = [f"/download/{os.path.basename(f)}" for f in output_files]
        return JSONResponse(content={"download_links": download_links})
    else:
        raise HTTPException(status_code=400, detail="Invalid file format")
    
@app.get("/download_video")
async def download_video(video_name: str):
    # Define the path to your video directory
    video_directory = "/path/to/your/video/files"
    video_path = r"C:\\Users\91735\\cine-copilot-app - Copy\\backend\\output_video_.mp4"
    
    # Use FileResponse to send the file back to the client
    return FileResponse(video_path, media_type='video/mp4', filename=f"{video_name}.mp4")
    
@app.post("/upload_video")
async def upload_video(file: UploadFile = File(...)):
    print("SFDsdfsdf")
    if file.filename.endswith('.mp4'):  # Ensure it is a video file
        print("werwer")
        save_path_1 = os.path.join(UPLOAD_DIR, file.filename)
        with open(save_path_1, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            # save_path_pho = os.path.join(UPLOAD_pho, file.filename)
            print("processing ....")
        photo_list = list_file_paths(r"C:\\Users\91735\\cine-copilot-app - Copy\backend\\upo_img")
        print(photo_list)
        smart_obj.smart_pro(save_path_1,photo_list)

# @app.post("/upload_images")
# async def create_upload_file(file: UploadFile = File(...)):
#     # Define the directory to save the file
#     out_dir = "uploaded_images"
#     os.makedirs(out_dir, exist_ok=True)
    
#     # Define the path to save the file
#     out_file = os.path.join(out_dir, file.filename)

#     # Save the uploaded file to the specified directory
#     with open(out_file, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {"filename": file.filename}
    

# @app.post("/smart")
# async def upload_media(file: UploadFile = File(...)):
#     # Ensure the file is either a video or a photo
#     if file.filename.endswith('.mp4'):  # Ensure it is a video file
#         save_path = os.path.join(UPLOAD_DIR, file.filename)
#         with open(save_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
#     elif file.filename.endswith(('.jpeg', '.jpg', '.png')):
#         save_path_pho = os.path.join(UPLOAD_pho, file.filename)
#         with open(save_path_pho, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
#     else:
#         raise Exception("Unsupported file format. Please upload a video or photo.")
    
#     photo_list = list_file_paths(save_path_pho)
#     smart_obj.smart_pro(save_path_vid,photo_list)


def list_file_paths(directory: str):
    # Create a Path object
    base_path = Path(directory)
    # List all file paths recursively
    file_paths = [str(file) for file in base_path.rglob('*') if file.is_file()]
    return file_paths


@app.post("/light")
async def upload_video(file: UploadFile = File(...)):
    if file.filename.endswith('.mp4'):  # Ensure it is a video file
        save_path_1 = os.path.join(UPLOAD_DIR, file.filename)
        with open(save_path_1, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        light_obj.light_proc(save_path_1)


@app.post("/cam")
async def upload_video(file: UploadFile = File(...)):
    print("sdfsfddf")
    if file.filename.endswith('.mp4'):  # Ensure it is a video file
        save_path_1 = os.path.join(UPLOAD_DIR, file.filename)
        with open(save_path_1, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        cam_obj.camer_pro(save_path_1)

@app.post("/shot")
async def upload_video(file: UploadFile = File(...)):
    # print("sdfsfddf")
    if file.filename.endswith('.mp4'):  # Ensure it is a video file
        save_path_1 = os.path.join(UPLOAD_DIR, file.filename)
        with open(save_path_1, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        shot_obj.shot_pro(save_path_1)
    

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=filename, media_type='application/octet-stream')
    else:
        raise HTTPException(status_code=404, detail="File not found")
    


# This section is useful when running the script directly, comment out if causing issues when running through Uvicorn externally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)


