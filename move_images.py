import os
import shutil
import random

def split_data_for_vehicles(source_dir, train_dir, validation_dir, split_ratio=0.8):
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validation_dir, exist_ok=True)

    category = "vehicles"
    category_path = os.path.join(source_dir, category)

    train_category_dir = os.path.join(train_dir, category)
    validation_category_dir = os.path.join(validation_dir, category)
    os.makedirs(train_category_dir, exist_ok=True)
    os.makedirs(validation_category_dir, exist_ok=True)

    images = [img for img in os.listdir(category_path) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not images:
        print(f"No images in {category_path}")
        return

    random.shuffle(images)

    split_point = int(len(images) * split_ratio)
    train_images = images[:split_point]
    validation_images = images[split_point:]

    for img in train_images:
        shutil.copy(os.path.join(category_path, img), os.path.join(train_category_dir, img))

    for img in validation_images:
        shutil.copy(os.path.join(category_path, img), os.path.join(validation_category_dir, img))

    print(f"Categoria '{category}': {len(train_images)} imagini în train, {len(validation_images)} imagini în validation.")

source_directory = "data"
train_directory = os.path.join(source_directory, "train")
validation_directory = os.path.join(source_directory, "validation")

split_data_for_vehicles(source_directory, train_directory, validation_directory, split_ratio=0.8)
