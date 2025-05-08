
import streamlit as st
import cv2
import numpy as np
from detect_plate import load_model, detect_number_plate
from ocr_engine import extract_text_from_image

st.title('Vehicle Number Plate Detection')

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    st.image(img, channels='BGR', caption="Uploaded Image")

    model = load_model()
    results = detect_number_plate(model, img)

    st.write("Detection Results:")
    st.image(np.squeeze(results.render()), channels='BGR')

    for crop in results.crop(save=False):
        text = extract_text_from_image(crop)
        st.write(f"Detected Text: {text}")
