import sys
import os
import numpy as np
import tensorflow as tf
import cv2

# Add the root project directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.data_preprocessing import load_and_preprocess_image  # Now it can import from scripts
from models.utils import load_model

def detect_scratch(image_path):
    
    # Load the trained model
    model = load_model('D:\\Scratch_Detection\\scratch_detection_project\\scratch_detection_project\\outputs\\model_checkpoints\\scratch_detection_model.h5')

    # Load and preprocess the image
    img = load_and_preprocess_image(image_path)
    
    # Perform inference
    prediction = model.predict(img)
    
    # Check prediction result
    if prediction[0] > 0.5:
        return "Scratch Detected"
    else:
        return "No Scratch Detected"

if __name__ == "__main__":
    image_path = 'D:\\Scratch_Detection\\scratch_detection_project\\scratch_detection_project\\data\\test\\bad_images\\09_08_2024_18_11_16.560412_classifier_input.png'  # Provide the image path to check
    result = detect_scratch(image_path)
    print(result)
