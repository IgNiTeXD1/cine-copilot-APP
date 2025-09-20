import torch
import torchvision.transforms as transforms
from PIL import Image
import cv2
import os
import pandas as pd

# Define the model architecture
class ResNet(torch.nn.Module):
    def __init__(self, num_angle_classes=5, num_level_classes=6):
        super(ResNet, self).__init__()
        self.resnet = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', weights=None)
        self.resnet.fc = torch.nn.Linear(self.resnet.fc.in_features, 512)
        self.angle_head = torch.nn.Linear(512, num_angle_classes)
        self.level_head = torch.nn.Linear(512, num_level_classes)

    def forward(self, x):
        x = self.resnet(x)
        angle_logits = self.angle_head(x)
        level_logits = self.level_head(x)
        return angle_logits, level_logits

# Initialize and load the model
model = ResNet(num_angle_classes=5, num_level_classes=6)
checkpoint = torch.load(r"C:\Users\91735\Desktop\camlvl\model.ckpt", map_location=torch.device('cpu'))
model.load_state_dict(checkpoint['state_dict'])
model.eval()

# Define image transformation
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Mapping class indices to names
ANGLE_CLASSES = {0: "Wide Shot", 1: "Medium Shot", 2: "Close-up", 3: "Over-the-Shoulder", 4: "Low Angle"}
LEVEL_CLASSES = {0: "Eye Level", 1: "High Angle", 2: "Low Angle", 3: "Dutch Tilt", 4: "Bird's Eye View", 5: "Worm's Eye View"}

# Function to process a video frame
def process_frame(frame):
    image = Image.fromarray(frame)
    t_image = transform(image).unsqueeze(0)
    with torch.no_grad():
        angle, level = model(t_image)
    return ANGLE_CLASSES[torch.argmax(angle, dim=1).item()], LEVEL_CLASSES[torch.argmax(level, dim=1).item()]

# Process video and save frame-by-frame analysis to CSV
def analyze_video(video_path, output_csv):
    print('Processing....')
    cap = cv2.VideoCapture(video_path)
    frame_number = 0
    data = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        angle, level = process_frame(frame)
        data.append({'Frame': frame_number, 'Angle': angle, 'Level': level})
        frame_number += 1
    
    cap.release()
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)
    print(f"Analysis saved to {output_csv}")

# Example usage
# video_path = r"C:\Users\91735\Desktop\camlvl\Ultimate Guide to Camera Angles_ Every Camera Shot Explained [Shot List, Ep. 3].mp4"
output_csv = "frame_analysisf.csv"
# analyze_video(video_path, output_csv)

class camer11():
    def __init__(self):
        pass
    
    def camer_pro(self,video_path):
        analyze_video(video_path, output_csv)




