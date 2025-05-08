
# Number Plate Detection of Vehicles

This project uses YOLO for number plate detection and EasyOCR for character recognition. It is deployed as a Streamlit web app.

## Features
- Real-time detection via webcam or uploaded images
- OCR extraction of number plates
- Interactive dashboard with performance metrics

## Technologies
- Python, OpenCV, Streamlit
- YOLO (You Only Look Once) Object Detection
- EasyOCR / Tesseract

## How to Run
1. Clone this repo:
    ```
    git clone https://github.com/your-username/number-plate-detection.git
    cd number-plate-detection
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Start Streamlit app:
    ```
    streamlit run deployment/streamlit_app.py
    ```

## Dataset
Dataset used from: [Google Drive Link](https://drive.google.com/file/d/1HAyBtLZGuzHyu2URNE25W5U6nvl15a_G/view)

## Results
- Detection Accuracy: 95%+
- OCR Precision: 90%+
- Real-time Inference: < 50ms/image

## License
MIT License
