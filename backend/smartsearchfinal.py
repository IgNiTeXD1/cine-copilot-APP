import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D
from sklearn.metrics.pairwise import cosine_similarity
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Load Pre-trained MobileNetV2 as a Feature Extractor
def load_feature_extractor():
    base_model = MobileNetV2(weights="imagenet", include_top=False)
    output_layer = GlobalAveragePooling2D()(base_model.output)
    model = Model(inputs=base_model.input, outputs=output_layer)
    return model

# Preprocess an image for MobileNetV2
def preprocess_image(image):
    image = cv2.resize(image, (224, 224))  # Resize to MobileNetV2 input size
    image = image.astype("float32") / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Extract feature embedding from an image
def extract_features(model, image):
    try:
        preprocessed_image = preprocess_image(image)
        embedding = model.predict(preprocessed_image, verbose=0)
        return embedding.flatten()
    except Exception as e:
        print(f"Feature Extraction Error: {e}")
        return None

# Compute Cosine Similarity
def is_similar(reference_embeddings, frame_embedding, threshold=0.7):
    if frame_embedding is None:
        return False  # Skip invalid comparisons

    for reference_embedding in reference_embeddings:
        similarity = cosine_similarity([reference_embedding], [frame_embedding])[0][0]
        if similarity >= threshold:
            return True
    return False

# Optimized Video Frame Extraction Using OpenCV
def find_all_matching_segments(video_path, reference_embeddings, model, threshold=0.7, frame_skip=5):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Error: Video file '{video_path}' not found.")

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps)
    matched_segments = []

    is_matching = False
    start_time = 0
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % frame_skip != 0:  # Skip frames to speed up
            continue

        frame_embedding = extract_features(model, frame)
        if is_similar(reference_embeddings, frame_embedding, threshold):
            if not is_matching:
                start_time = frame_count / fps
                is_matching = True
        else:
            if is_matching:
                matched_segments.append((start_time, frame_count / fps))
                is_matching = False

    # If video ends while still detecting, save the last segment
    if is_matching:
        matched_segments.append((start_time, duration))

    cap.release()
    return matched_segments

# Extract and save video clips using MoviePy
def extract_and_save_segments(video_path, matched_segments):
    if not matched_segments:
        print("⚠ No matching segments found.")
        return

    video = VideoFileClip(video_path)
    clips = [video.subclip(start, end) for start, end in matched_segments]

    final_clip = concatenate_videoclips(clips, method="compose")
    output_file = "output_video_.mp4"
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
    print(f"✅ Process completed! Extracted video saved as '{output_file}'")

# Main Function
def main(video_path,reference_image_paths):
    # video_path = r"C:\Users\91735\Desktop\smart\Appa Lock Tamil Short Film (2017) By  Pradeep Ranganathan.mp4"
    # reference_image_paths = [
    #     r"C:\Users\91735\Desktop\smart\frame_1449.jpg",
    #     r"C:\Users\91735\Desktop\smart\frame_2323.jpg",
    #     r"C:\Users\91735\Desktop\smart\frame_2346.jpg",
    #     r"C:\Users\91735\Desktop\smart\frame_2369.jpg",
    #     r"C:\Users\91735\Desktop\smart\frame_2139.jpg",
    #     r"C:\Users\91735\Desktop\smart\frame_1955.jpg"

    # ]

    print("🔍 Loading MobileNetV2 feature extractor...")
    model = load_feature_extractor()

    reference_embeddings = []
    for img_path in reference_image_paths:
        if not os.path.exists(img_path):
            print(f"⚠ Warning: Reference image '{img_path}' not found. Skipping...")
            continue

        print(f"📷 Processing reference image: {img_path}")
        reference_image = cv2.imread(img_path)
        embedding = extract_features(model, reference_image)
        if embedding is not None:
            reference_embeddings.append(embedding)

    if not reference_embeddings:
        raise ValueError("Error: No valid reference images found. Cannot proceed.")

    print("🎥 Searching for ALL screen time segments where the character/prop appears...")
    matched_segments = find_all_matching_segments(video_path, reference_embeddings, model, frame_skip=5)

    print("🎬 Extracting and saving all detected segments into a single video...")
    extract_and_save_segments(video_path, matched_segments)

# if __name__ == "__main__":
#     main()

class smart():
    def __init__(self):
        pass

    def smart_pro(self,video_path,reference_image_paths):
        main(video_path,reference_image_paths)

