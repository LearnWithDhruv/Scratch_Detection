import matplotlib.pyplot as plt
import tensorflow as tf
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.data_preprocessing import load_and_preprocess_image  # Now it can import from scripts
from models.utils import load_model

def visualize_results(image_path, save_dir):
    img = load_and_preprocess_image(image_path)
    model = load_model('D:\Scratch_Detection\scratch_detection_project\scratch_detection_project\outputs\model_checkpoints\scratch_detection_model.h5')

    prediction = model.predict(img)  
    
    # Set the prediction title
    prediction_title = 'Scratch Detected' if prediction[0] > 0.5 else 'No Scratch Detected'

    # Plot the image with the prediction title
    plt.imshow(img[0])  
    plt.title(f"Prediction: {prediction_title}")
    plt.axis('off')
    
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Save the prediction image with title in the specified directory
    image_name = os.path.basename(image_path)  # Get the image file name
    save_path = os.path.join(save_dir, f"predicted_{image_name}")
    plt.savefig(save_path)

    # Optionally, display the image
    plt.show()

if __name__ == "__main__":
    image_path = 'D:\\Scratch_Detection\\scratch_detection_project\\scratch_detection_project\\data\\test\\bad_images\\09_08_2024_18_11_16.560412_classifier_input.png'  # Provide the image path to check
    save_dir = 'D:\\Scratch_Detection\\scratch_detection_project\\scratch_detection_project\\outputs\\results\\predictions'  # Directory to save predictions
    visualize_results(image_path, save_dir)
