from ultralytics import YOLO
import cv2
import os
import shutil
from tqdm import tqdm

def person_area_ratio(image_path: str, model_path: str = "yolov8s.pt", total_area: float = None):
    # Load YOLO model
    model = YOLO(model_path)
    
    # Predict objects in image
    results = model(image_path, verbose=False)
    
    # Find person (object class 0) and get area of bounding box
    area_ratio = 0
    for r in results:
        # Get the Boxes object containing the detection boxes
        boxes = r.boxes
        
        # Filter the boxes by class value 0 (person)
        person_boxes = boxes[boxes.cls == 0]
        
        # Check if there is any person box
        if len(person_boxes) > 0:
            # Get the first person box
            x1, y1, x2, y2 = person_boxes.data[0][:4]
            
            # Calculate the area of the bounding box
            area = (x2 - x1) * (y2 - y1)
            
            # Calculate the total image area if not provided
            if total_area is None:
                image = cv2.imread(image_path)
                h, w = image.shape[:2]
                total_area = h * w
            
            # Calculate the ratio of the bounding box area to the total image area
            area_ratio = round(float(area / total_area), 2)
            
            # Break the loop
            break
    
    return area_ratio

def main():
    source_dir = "./images/"
    destination_dir = "./new-images/"
    
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Calculate total image area for first image in source directory
    total_area = None
    for filename in os.listdir(source_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(source_dir, filename)
            image = cv2.imread(image_path)
            h, w = image.shape[:2]
            total_area = h * w
            break
    
    # Iterate over images in source directory with tqdm progress bar
    with tqdm(os.listdir(source_dir), desc="Filtering images", unit="image") as pbar:
        for filename in pbar:
            # Check if file is an image
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                # Get image path
                image_path = os.path.join(source_dir, filename)
                
                # Calculate ratio of bounding box area of detected person to total image area
                area_ratio = person_area_ratio(image_path, "yolov8s.pt", total_area)
                
                # Check if ratio is below 0.35
                if area_ratio < 0.35:
                    # Copy image to destination directory
                    shutil.copy(image_path, destination_dir)
                    pbar.write(f"Copied {filename} to {destination_dir}")

if __name__ == "__main__":
    main()

