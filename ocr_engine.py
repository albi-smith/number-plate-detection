
import easyocr
import cv2

reader = easyocr.Reader(['en'])

def extract_text_from_image(img):
    result = reader.readtext(img)
    text_results = [text[1] for text in result]
    return text_results
