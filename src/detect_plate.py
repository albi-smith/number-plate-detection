
import torch
from PIL import Image
import cv2

def load_model(model_path='models/yolov5s.pt'):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    return model

def detect_number_plate(model, img):
    results = model(img)
    return results
