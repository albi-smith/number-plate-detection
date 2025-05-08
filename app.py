
from detect_plate import load_model, detect_number_plate
from ocr_engine import extract_text_from_image
import cv2

def process_image(img_path):
    model = load_model()
    img = cv2.imread(img_path)
    results = detect_number_plate(model, img)
    crops = results.crop(save=False)
    ocr_results = []
    for crop in crops:
        ocr_text = extract_text_from_image(crop)
        ocr_results.append(ocr_text)
    return ocr_results
