import os
import tarfile
import zipfile
import send2trash
from tqdm import tqdm

def check_files(directory):
    corrupted = []
    for filename in tqdm(os.listdir(directory), desc="Checking files"):
        path = os.path.join(directory, filename)
        if filename.endswith('.zip'):
            with zipfile.ZipFile(path, 'r') as zip_ref:
                if zip_ref.testzip():
                    corrupted.append(filename)
        elif filename.endswith(('.tar', '.tar.gz', '.tar.bz2')):
            try:
                with tarfile.open(path, 'r'):
                    pass
            except tarfile.ReadError:
                corrupted.append(filename)
    if corrupted:
        print(f'Corrupted files: {", ".join(corrupted)}')
        return False
    return True

def extract_files(directory):
    for filename in tqdm(os.listdir(directory), desc="Extracting files"):
        path = os.path.join(directory, filename)
        extracted_dir = os.path.splitext(filename)[0]
        extracted_path = os.path.join(directory, extracted_dir)
        if filename.endswith('.zip'):
            with zipfile.ZipFile(path, 'r') as zip_ref:
                os.makedirs(extracted_path, exist_ok=True)
                zip_ref.extractall(extracted_path)
        elif filename.endswith(('.tar', '.tar.gz', '.tar.bz2')):
            with tarfile.open(path, 'r') as tar_ref:
                os.makedirs(extracted_path, exist_ok=True)
                tar_ref.extractall(extracted_path)

def delete_archives(directory):
    for filename in tqdm(os.listdir(directory), desc="Deleting archives"):
        if filename.endswith(('.tar', '.tar.gz', '.tar.bz2')):
            file_path = os.path.join(directory, filename)
            send2trash.send2trash(file_path)

def process_directories(base_directory):
    for sub_directory in tqdm(os.listdir(base_directory), desc="Processing directories"):
        sub_dir_path = os.path.join(base_directory, sub_directory, 'rgb_frames')
        if os.path.exists(sub_dir_path) and os.path.isdir(sub_dir_path):
            print(f"Processing {sub_dir_path}")
            if check_files(sub_dir_path):
                extract_files(sub_dir_path)
                delete_archives(sub_dir_path)
                print(f"Unzipped and Cleaned {sub_dir_path}!")
        else:
            print("Could not find the folders correctly")

# Main input directory
main_directory = '../EPIC-KITCHENS'
process_directories(main_directory)
