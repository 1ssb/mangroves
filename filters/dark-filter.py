import os
from PIL import Image
import numpy as np

def remove_dark_images(directory, threshold):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            image = Image.open(file_path)
            image_data = np.asarray(image)
            avg_pixel_value = np.mean(image_data)
            if avg_pixel_value < threshold:
                os.remove(file_path)
                print(f"Removed {filename}")

# Example usage
remove_dark_images("./images/", 50)

