import os
from PIL import Image

def resize_and_center_crop_images(directory, size):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            image = Image.open(file_path)
            width, height = image.size
            if width > height:
                left = (width - height) / 2
                top = 0
                right = (width + height) / 2
                bottom = height
            else:
                left = 0
                top = (height - width) / 2
                right = width
                bottom = (height + width) / 2
            image = image.crop((left, top, right, bottom))
            image = image.resize(size, Image.LANCZOS)
            image.save(file_path)
            print(f"Resized and center cropped {filename}")

# Example usage
s = 256
resize_and_center_crop_images("./images/", (s, s))

