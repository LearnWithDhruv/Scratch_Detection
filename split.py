import random
import os
import shutil
import zipfile

# Define the path to the extracted folder
extracted_folder_path = 'D:\Scratch_Detection\scratch_detection_project\anomaly_detection_test_data'  # This is the extracted folder

# Define the destination folder for the train, test, and augmented datasets
train_dir = 'data/train'
test_dir = 'data/test'

# Create necessary directories for train and test (if not already created)
os.makedirs(f'{train_dir}/good_images', exist_ok=True)
os.makedirs(f'{train_dir}/bad_images', exist_ok=True)
os.makedirs(f'{test_dir}/good_images', exist_ok=True)
os.makedirs(f'{test_dir}/bad_images', exist_ok=True)

def split_data(source_folder, dest_folder, train_ratio=0.8):
    
    # Get all files in the source folder
    files = os.listdir(source_folder)
    
    # Shuffle files for randomness
    random.shuffle(files)
    
    # Calculate the split index based on the train ratio
    split_index = int(len(files) * train_ratio)
    
    # Split into train and test files
    train_files = files[:split_index]
    test_files = files[split_index:]
    
    # Move files to train and test directories
    for file in train_files:
        # Move file to the correct train folder
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder, 'train', os.path.basename(source_folder), file))
    
    for file in test_files:
        # Move file to the correct test folder
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder, 'test', os.path.basename(source_folder), file))

# Organize the `good_images` and `bad_images` into train and test sets
good_images_dir = os.path.join(extracted_folder_path, 'good_images')
bad_images_dir = os.path.join(extracted_folder_path, 'bad_images')

# Split the `good_images` and `bad_images` into train and test sets
split_data(good_images_dir, 'data')
split_data(bad_images_dir, 'data')

print("Data split into train and test sets.")
