import torch
import torchvision.transforms as transforms
import cv2
import numpy as np
import pandas as pd
from PIL import Image
from torchvision.models import resnet50, ResNet50_Weights
from moviepy.editor import VideoFileClip

resnet50 = resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
resnet50.fc = torch.nn.Linear(resnet50.fc.in_features, 6)  
resnet50.eval()

lighting_classes = ["High-Key", "Low-Key", "Soft Lighting", "Hard Lighting", "Silhouette", "Chiaroscuro"]

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def predict_lighting(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = resnet50(image_tensor)
        _, predicted = torch.max(output, 1)
    return lighting_classes[predicted.item()]

def detect_light_position(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape
    left = np.mean(gray[:, :width//3])
    center = np.mean(gray[:, width//3:2*width//3])
    right = np.mean(gray[:, 2*width//3:])
    if center > left and center > right:
        return "Front Light"
    elif left > center and left > right:
        return "Side Light (Left)"
    elif right > center and right > left:
        return "Side Light (Right)"
    else:
        return "Back Light"

def calculate_lighting_ratio(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bright_pixels = gray[gray > 180]
    dark_pixels = gray[gray < 80]
    if bright_pixels.size == 0 or dark_pixels.size == 0:  
        return "Key-to-Fill Ratio: Undefined"
    ratio = np.mean(bright_pixels) / (np.mean(dark_pixels) + 1e-5)
    return f"Key-to-Fill Ratio: {min(round(ratio, 2), 50)}:1"

def detect_shadow_intensity(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    shadow_intensity = np.sum(edges) / (gray.shape[0] * gray.shape[1])
    return "Soft Shadows" if shadow_intensity < 0.02 else "Hard Shadows"

def estimate_color_temperature(frame):
    avg_color = np.mean(frame, axis=(0, 1))
    red, green, blue = avg_color
    if red == 0:  
        return "Unknown"
    kelvin = (blue / red) * 10000  
    return "Warm Lighting" if kelvin < 5000 else "Cool Lighting"

def calculate_contrast_ratio(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    min_brightness = np.min(gray)
    max_brightness = np.max(gray)
    if min_brightness == max_brightness:  
        return "Contrast Ratio: Undefined"
    ratio = max_brightness / (min_brightness + 1)
    return f"Contrast Ratio: {min(round(ratio, 2), 50)}:1"

def detect_glaring(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    glare_threshold=240
    glare_pixels=np.sum(gray > glare_threshold) / gray.size
    return "Glare Present" if glare_pixels > 0.1 else "No Glare"

def overlay_text(frame, text, position=(10, 30), font_scale=0.7, color=(0, 255, 255)):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, 2, cv2.LINE_AA)

def process_video_with_overlay(video_path, output_video="final_annotated_video.mp4", output_csv="frame_analysis_final.csv"):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}.")
        return

    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Processing {total_frames} frames...")

    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("temp_annotated_video.mp4", fourcc, fps, (width, height))

    results = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Extract features
        lighting = predict_lighting(frame)
        key_light = detect_light_position(frame)
        lighting_ratio = calculate_lighting_ratio(frame)
        shadow_intensity = detect_shadow_intensity(frame)
        color_temp = estimate_color_temperature(frame)
        contrast_ratio = calculate_contrast_ratio(frame)
        glare = detect_glaring(frame)

        # Save frame-wise data
        results.append([
            frame_count, lighting, key_light, lighting_ratio, 
            shadow_intensity, color_temp, contrast_ratio, glare
        ])

        # Overlay extracted information on video frame
        text_overlay = (f"Lighting: {lighting} | Key Light: {key_light} | "
                        f"Ratio: {lighting_ratio} | Shadow: {shadow_intensity} | "
                        f"Temp: {color_temp} | Contrast: {contrast_ratio} | Glare: {glare}")
        overlay_text(frame, text_overlay, position=(10, 30))

        # Write annotated frame to video
        out.write(frame)
        frame_count += 1

    cap.release()
    out.release()

    # Save frame-wise analysis as CSV
    df = pd.DataFrame(results, columns=[
        "Frame", "Lighting", "Key Light Position", "Lighting Ratio",
        "Shadow Intensity", "Color Temperature", "Contrast Ratio", "Glare Detection"
    ])
    df.to_csv(output_csv, index=False)
    print(f"Frame-wise analysis saved as '{output_csv}'")

    # Merge Video & Original Audio
    original_video = VideoFileClip(video_path)
    annotated_video = VideoFileClip("temp_annotated_video.mp4").set_audio(original_video.audio)
    annotated_video.write_videofile(output_video, codec="libx264", fps=fps)

    print(f"Final annotated video with original audio saved as '{output_video}'")

# # Run analysis with video overlay & frame-wise CSV output
# video_path = r"C:\Users\91735\Desktop\light\Appa Lock Tamil Short Film (2017) By  Pradeep Ranganathan.mp4"
# process_video_with_overlay(video_path)


class light:
    def __init__(self):
        # self.fun = process_video_with_overlay()
        pass
    def light_proc(self,video_path):
        process_video_with_overlay(video_path)
        return None

