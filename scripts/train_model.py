import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.scratch_detection_model import build_model

import tensorflow as tf
from models.scratch_detection_model import build_model
from scripts.augment_data import augment_images
from scripts.data_preprocessing import load_dataset_from_directory
from models.utils import save_model

def train_model(train_dir, epochs=10, batch_size=32):
    
    # Load training data
    train_images, train_labels = load_dataset_from_directory(train_dir)

    # Build the model
    model = build_model(input_shape=(128, 128, 3))

    # Apply data augmentation to the training set
    train_data = augment_images(train_dir)

    model.fit(train_data, epochs=epochs, batch_size=batch_size)

    # Set the path where the model should be saved
    model_save_path = r'D:\Scratch_Detection\scratch_detection_project\scratch_detection_project\outputs\model_checkpoints\scratch_detection_model.h5'
    
    # Save the model to the specified path
    save_model(model, model_save_path)

if __name__ == "__main__":
    train_model('data/train')
