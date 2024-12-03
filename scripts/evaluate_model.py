import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models')))

from utils import load_model
import tensorflow as tf
# from models.utils import load_model
from data_preprocessing import load_dataset_from_directory

def evaluate_model(test_dir):
    
    # Load the trained model
    model = load_model('D:\Scratch_Detection\scratch_detection_project\scratch_detection_project\outputs\model_checkpoints\scratch_detection_model.h5')

    # Load and preprocess the test dataset
    test_images, test_labels = load_dataset_from_directory(test_dir)

    # Evaluate the model on the test data
    loss, accuracy = model.evaluate(test_images, test_labels)
    print(f"Test Loss: {loss}")
    print(f"Test Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    evaluate_model('data/test')
