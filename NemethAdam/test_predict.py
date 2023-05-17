import cv2
from ultralytics import YOLO


# Load the YOLOv8 model
model = YOLO('D:\\SAJAT\\00_ML\\MY PROJECTS\\People recognization\\intern\\runs\\content\\runs\\detect\\train\\weights\\best.pt')

# the path to the video
orig_dir = "D:\\SAJAT\\00_ML\MY PROJECTS\\People recognization\\test_videos\\test4.mp4"

# get the result from YOLOv8
results = model.predict(orig_dir, save=True, imgsz=320, conf=0.3)