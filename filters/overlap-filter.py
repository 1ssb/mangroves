import os
import json
import numpy as np
from scipy.spatial.transform import Rotation as R
from tqdm import tqdm
from shutil import copyfile

def calculate_frustum_overlap(frustum1, frustum2, K):
    # Calculate the overlap between two camera frustums using the projection method
    corners1 = np.dot(frustum1, K.T)
    corners1 = corners1[:, :2] / corners1[:, 2:]
    min_x1, min_y1 = np.min(corners1, axis=0)
    max_x1, max_y1 = np.max(corners1, axis=0)
    corners2 = np.dot(frustum2, K.T)
    corners2 = corners2[:, :2] / corners2[:, 2:]
    min_x2, min_y2 = np.min(corners2, axis=0)
    max_x2, max_y2 = np.max(corners2, axis=0)
    dx = min(max_x1, max_x2) - max(min_x1, min_x2)
    dy = min(max_y1, max_y2) - max(min_y1, min_y2)
    if dx >= 0 and dy >= 0:
        overlap_area = dx * dy
        area1 = (max_x1 - min_x1) * (max_y1 - min_y1)
        overlap_ratio = overlap_area / area1
        return overlap_ratio
    else:
        return 0.0

def select_frames(file_path, overlap_threshold=0.60, target_ratio=1/3):
    with open(file_path, 'r') as f:
        data = json.load(f)
    camera = data['camera']
    fx, fy, cx, cy = camera['params'][:4]
    K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
    images = data['images']
    selected_frames = []
    
    print("Calculating camera frustums for all frames...")
    for frame_name in tqdm(images.keys()):
        pose = images[frame_name]
        q = pose[:4]
        t = pose[4:]
        r = R.from_quat(q)
        rot_mat = r.as_matrix()
        trans_vec = np.array(t).reshape(3, 1)
        transform_mat = np.hstack((rot_mat, trans_vec))
        transform_mat = np.vstack((transform_mat, [0, 0, 0, 1]))
        transform_mat = np.linalg.inv(transform_mat)
        transform_mat[1,:] *= -1
        transform_mat[:, 1] *= -1
        # Calculate the camera frustum for the current frame
        n=0.01 # near plane
        f=100.0 # far plane
        t=n/fx*(camera['height']/2-cy)
        b=-t
        r_=n/fy*(camera['width']/2-cx)
        l_=-r_
        n_corners=np.array([[l_,b,-n],[l_,t,-n],[r_,t,-n],[r_,b,-n]])
        f_corners=np.array([[l_,b,-f],[l_,t,-f],[r_,t,-f],[r_,b,-f]])
        corners_cam=np.vstack((n_corners,f_corners))
        corners_cam_homo=np.hstack((corners_cam,np.ones((corners_cam.shape[0], 1))))
        corners_world_homo=np.dot(corners_cam_homo , transform_mat.T)
        selected_frames.append((frame_name,corners_world_homo))
    
    target_num_frames=int(len(selected_frames)*target_ratio)
    
    print("Removing frames with high overlap...")
    batch_num = 0
    while len(selected_frames)>target_num_frames:
      print(f"Processing batch {batch_num}...")
      overlaps=[]
      for i in tqdm(range(0,len(selected_frames)-len(selected_frames)%2-1,2)):
          frame1_frustum=selected_frames[i][1]
          frame2_frustum=selected_frames[i+1][1]
          overlap=calculate_frustum_overlap(frame1_frustum[:,:3],frame2_frustum[:,:3],K)
          overlaps.append(overlap)

      remove_indices=[]
      for i in range(len(overlaps)):
          if i+1 < len(overlaps) and overlaps[i]>overlap_threshold:
              remove_indices.append(2*i+np.argmax([overlaps[i],overlaps[i+1]]))
      
      for idx in sorted(remove_indices)[::-1]:
          del selected_frames[idx]
      
      if len(selected_frames)%2==1:
          del selected_frames[-1]
      
      batch_num += 1

    return [frame[0] for frame in selected_frames]

json_data_dir = './JSON_DATA'
frames_dir = './frames'
selected_frames_dir = './selected_frames'

for file_name in tqdm(os.listdir(json_data_dir)):
    file_path = os.path.join(json_data_dir, file_name)
    folder_name = os.path.splitext(file_name)[0]
    src_folder_path = os.path.join(frames_dir, folder_name)
    dst_folder_path = os.path.join(selected_frames_dir, folder_name)
    if not os.path.exists(dst_folder_path):
        os.makedirs(dst_folder_path)
    selected_frames = select_frames(file_path)
    for frame in tqdm(selected_frames):
        # Copy the selected frame to the destination folder
        src_file_path = os.path.join(src_folder_path, frame)
        dst_file_path = os.path.join(dst_folder_path, frame)
        copyfile(src_file_path, dst_file_path)
