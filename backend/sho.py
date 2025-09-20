import numpy as np
import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image as pil_image
import imageio
from tqdm import tqdm

# Define shot scale classes
id2cls = ['Close Shot (CS)', 'Medium Shot (MS)', 'Long Shot (LS)']

def shot_scale(image, model, dims=(125, 224)):
    """
    Extract shot scale predictions from an image.
    
    Args:
    ---
    image: input RGB image
    model: loaded TensorFlow model
    dims: image target dimensions
    
    Returns:
    ---
    Shot scale class index
    """
    width_height_tuple = (dims[1], dims[0])
    cval = 0

    try:
        # Resize and process the image
        raw_img = pil_image.fromarray(image)
        img = raw_img.copy()
        img.thumbnail(width_height_tuple, pil_image.NEAREST)

        final_img = pil_image.new(img.mode, width_height_tuple,
                                  (cval if img.mode == 'L'
                                   else (cval, cval, cval)))

        final_img.paste(
            img,
            ((width_height_tuple[0] - img.size[0]) // 2,
             (width_height_tuple[1] - img.size[1]) // 2)
        )
        image_c = np.asarray(final_img, dtype='float32') / 255.
        image_bn = np.asarray(final_img.convert('LA').convert('RGB'), dtype='float32') / 255.
        image = np.stack([image_c, image_bn], axis=0)

        pp = np.sum(model.predict(image), axis=0)
    except Exception as e:
        print(f"Error loading image: {e}")
        return -1  # Return -1 if there is an error

    return np.argmax(pp)  # Return the predicted class index

# Load the trained model without compilation to avoid optimizer issues
model_path = r"C:\Users\91735\Videos\cineco\shot\model_shotscale_967 (7).h5"  # Specify the path to the trained model
model = load_model(model_path, compile=False)

# Specify the video file path
video_path = r"c:\Users\91735\Downloads\Appa Lock Tamil Short Film (2017) By  Pradeep Ranganathan.mp4"  # Replace with your video file path

# Process video and retrieve shot scale model predictions and frames
def process_video(video_path, time_step=1):
    """
    Process video and return shot scale predictions for each frame.
    
    Args:
    ---
    video_path: path to the input video file
    model: loaded TensorFlow model
    time_step: seconds between frames to process
    
    Returns:
    ---
    List of dictionaries containing frame number and predicted shot scale class
    """
    try:
        vid = imageio.get_reader(video_path, 'ffmpeg')
        movie = os.path.basename(video_path)[:-4]
        model_path = r"C:\Users\91735\Videos\cineco\shot\model_shotscale_967 (7).h5"  # Specify the path to the trained model
        model = load_model(model_path, compile=False)

        print(f"Processing video: {movie}")

        out = []
        nframe = vid.get_meta_data()['duration'] * vid.get_meta_data()['fps']
        for num in tqdm(range(int(nframe // (vid.get_meta_data()['fps'] * time_step)))):  # Loop through frames
            try:
                image = vid.get_data(int(time_step * num * vid.get_meta_data()['fps']))
            except Exception as e:
                print(f"Error retrieving frame {num}: {e}")
                continue

            pred_idx = shot_scale(image, model)
            if pred_idx != -1:
                out.append({
                    "Frame": int(time_step * num * vid.get_meta_data()['fps']),
                    "Shot Scale": id2cls[pred_idx]
                })

        return out
    except Exception as e:
        print(f"Error processing video: {e}")
        return []

# # Process the video and save results to CSV
# frames_with_predictions = process_video(video_path, model)

# # Save output as CSV
# output_csv_path = "shot_scale_analysis.csv"
# df = pd.DataFrame(frames_with_predictions)
# df.to_csv(output_csv_path, index=False)
# print(f"Shot scale analysis saved to {output_csv_path}")

class shot():
    def __init__(self):
        pass

    def shot_pro(self,video_path):
        frames_with_predictions = process_video(video_path)

        # Save output as CSV
        output_csv_path = "shot_scale_analysis.csv"
        df = pd.DataFrame(frames_with_predictions)
        df.to_csv(output_csv_path, index=False)
        print(f"Shot scale analysis saved to {output_csv_path}")