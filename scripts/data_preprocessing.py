import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os
import numpy as np
import cv2

def is_valid_image(img_path, target_size=(128, 128)):
    try:
        img = image.load_img(img_path)  # Try loading the image
        return True
    except Exception as e:
        print(f"Error loading image {img_path}: {e}")
        return False
    
import numpy as np
import cv2

def load_and_preprocess_image(img_path, target_size=(128, 128)):
   
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Image not found at path: {img_path}")
    
    img = cv2.resize(img, target_size)
    
    img = img / 255.0
    
    # Ensure the image has the correct dtype (float32) for TensorFlow
    img = np.array(img, dtype=np.float32)
    
    # Check the shape and dtype of the image to confirm it's correct
    print(f"Image shape: {img.shape}, dtype: {img.dtype}")

    # Add batch dimension (the model expects input of shape (batch_size, height, width, channels))
    img = np.expand_dims(img, axis=0)  # Add batch dimension (1, 128, 128, 3)
    
    # Check final shape and dtype after processing
    print(f"Processed image shape: {img.shape}, dtype: {img.dtype}")

    return img


def load_dataset_from_directory(data_dir, target_size=(128, 128)):
   
    images = []
    labels = []
    
    # Iterate through good and bad images directories
    for label in ['good_images', 'bad_images']:
        label_path = os.path.join(data_dir, label)
        class_label = 0 if label == 'good_images' else 1  # 0 for good, 1 for bad
        
        for img_name in os.listdir(label_path):
            img_path = os.path.join(label_path, img_name)
            
            # Load and preprocess the image
            img = load_and_preprocess_image(img_path, target_size)
            
            # Check if the image is None (in case of errors) and skip it
            if img is not None:
                images.append(img)
                labels.append(class_label)
            else:
                print(f"Warning: Skipping invalid image {img_path}")

    # Convert lists to numpy arrays after processing all images
    images = np.array(images)
    labels = np.array(labels)
    
    return images, labels

def generate_mask_for_scratched_image(img_path, output_mask_path):
   
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Image not found at path: {img_path}")
    
    # Simple example mask generation: assume scratches are in the center
    mask = np.zeros(img.shape, dtype=np.uint8)
    height, width = mask.shape[:2]
    mask[height//4:3*height//4, width//4:3*width//4] = 255  # Example scratch area
    
    cv2.imwrite(output_mask_path, mask)
# import os
# import shutil
# import random
# from pathlib import Path

# # Define the base path where your original dataset is located
# base_path = 'D:\Scratch_Detection\scratch_detection_project\anomaly_detection_test_data'  # Replace with the actual path
# train_dir = 'data/train'
# test_dir = 'data/test'
# augmented_dir = 'data/augmented'

# # Create the necessary folders
# os.makedirs(f'{train_dir}/good_images', exist_ok=True)
# os.makedirs(f'{train_dir}/bad_images', exist_ok=True)
# os.makedirs(f'{test_dir}/good_images', exist_ok=True)
# os.makedirs(f'{test_dir}/bad_images', exist_ok=True)
# os.makedirs(f'{augmented_dir}/good_images', exist_ok=True)
# os.makedirs(f'{augmented_dir}/bad_images', exist_ok=True)

# # Function to split data into train/test
# def split_data(source_folder, dest_folder, train_ratio=0.8):
#     """
#     Split data into training and testing.
#     """
#     # Get all the files from the source folder
#     files = os.listdir(source_folder)
    
#     # Shuffle the file list for randomness
#     random.shuffle(files)
    
#     # Split into train and test sets based on the ratio
#     split_idx = int(len(files) * train_ratio)
    
#     train_files = files[:split_idx]
#     test_files = files[split_idx:]
    
#     # Move files to appropriate folders
#     for file in train_files:
#         shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder, 'train', os.path.basename(file)))
    
#     for file in test_files:
#         shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder, 'test', os.path.basename(file)))

# # Function to augment images and move to augmented folder
# def augment_data(source_folder, augmented_folder):
#     """
#     Apply augmentation to images and store them in the augmented folder.
#     """
#     # Example of augmentation (could be extended to actual transformations)
#     for file in os.listdir(source_folder):
#         # Just copy the files for now as placeholders for augmentation
#         shutil.copy(os.path.join(source_folder, file), os.path.join(augmented_folder, file))

# # Process good images
# good_images_dir = os.path.join(base_path, 'good_images')  # Adjust according to the folder you received
# split_data(good_images_dir, base_path)

# # Process bad images
# bad_images_dir = os.path.join(base_path, 'bad_images')  # Adjust according to the folder you received
# split_data(bad_images_dir, base_path)

# # Augment data (simple copy for now)
# augment_data(good_images_dir, augmented_dir + '/good_images')
# augment_data(bad_images_dir, augmented_dir + '/bad_images')
