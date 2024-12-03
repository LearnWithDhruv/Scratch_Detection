import os
import shutil
import random
import zipfile

# Define paths for the original folders and the new project directory
source_dir = r'D:\Scratch_Detection\scratch_detection_project\anomaly_detection_test_data'  # Replace with your unzipped folder containing good, bad, and masks
data_dir = r'D:\Scratch_Detection\scratch_detection_project\scratch_detection_project\data'  # Replace with the data directory of your project

# Define paths for train, test, and augmented directories
train_dir = os.path.join(data_dir, 'train')
test_dir = os.path.join(data_dir, 'test')
augmented_dir = os.path.join(data_dir, 'augmented')

# Define paths for good and bad images
good_source_dir = os.path.join(source_dir, 'good')
bad_source_dir = os.path.join(source_dir, 'bad')
masks_source_dir = os.path.join(source_dir, 'masks')

# Function to create directories if they do not exist
def create_dirs():
    dirs = [
        os.path.join(train_dir, 'good_images'),
        os.path.join(train_dir, 'bad_images'),
        os.path.join(test_dir, 'good_images'),
        os.path.join(test_dir, 'bad_images'),
        os.path.join(augmented_dir, 'good_images'),
        os.path.join(augmented_dir, 'bad_images'),
        os.path.join(train_dir, 'masks'),
        os.path.join(test_dir, 'masks'),
        os.path.join(augmented_dir, 'masks')
    ]
    for directory in dirs:
        if not os.path.exists(directory):
            print(f"Creating directory: {directory}")
            os.makedirs(directory)

# Function to move images into the respective directories
def move_images():
    # Debug: Check if the source directories exist
    print(f"Source directories: {os.listdir(good_source_dir)}, {os.listdir(bad_source_dir)}, {os.listdir(masks_source_dir)}")

    # Move good images to train, test, and augmented directories
    good_images = os.listdir(good_source_dir)
    random.shuffle(good_images)  # Shuffle to split into train/test
    print(f"Good images found: {len(good_images)}")

    # Split good images for train/test (80% train, 20% test)
    split_idx = int(0.8 * len(good_images))
    train_good = good_images[:split_idx]
    test_good = good_images[split_idx:]
    
    # Move good images into respective directories
    for img in train_good:
        shutil.move(os.path.join(good_source_dir, img), os.path.join(train_dir, 'good_images', img))
    for img in test_good:
        shutil.move(os.path.join(good_source_dir, img), os.path.join(test_dir, 'good_images', img))

    # Move bad images to train, test, and augmented directories
    bad_images = os.listdir(bad_source_dir)
    random.shuffle(bad_images)  # Shuffle to split into train/test
    print(f"Bad images found: {len(bad_images)}")
    
    # Split bad images for train/test (80% train, 20% test)
    split_idx = int(0.8 * len(bad_images))
    train_bad = bad_images[:split_idx]
    test_bad = bad_images[split_idx:]
    
    # Move bad images into respective directories
    for img in train_bad:
        shutil.move(os.path.join(bad_source_dir, img), os.path.join(train_dir, 'bad_images', img))
    for img in test_bad:
        shutil.move(os.path.join(bad_source_dir, img), os.path.join(test_dir, 'bad_images', img))
    
    # Move masks for bad images to respective directories
    masks = os.listdir(masks_source_dir)
    print(f"Masks found: {len(masks)}")
    for mask in masks:
        shutil.move(os.path.join(masks_source_dir, mask), os.path.join(train_dir, 'masks', mask))

# Call functions to create directories and move images
create_dirs()
move_images()

print("Process completed. Please verify the 'data' folder.")