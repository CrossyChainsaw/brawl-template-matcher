import os
import PIL
from PIL import Image


def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        # Check if the file is an image (you may need to add more file extensions)
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            # Read the image using OpenCV
            img = Image.open(img_path)
            if img is not None:
                images.append(img)
    return images


def get_image_paths(folder_path):
    image_paths = []
    for filename in os.listdir(folder_path):
        # Check if the file is an image (you may need to add more file extensions)
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            # Read the image using OpenCV
            img = Image.open(img_path)
            if img is not None:
                image_paths.append(img_path)
    return image_paths
