import cv2
import time
from rembg import remove
from PIL import Image
import numpy as np

def test_speed():
    video_path = 'assets/Vidéo_sans_son_personnages_dansants.mp4'
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        print("Could not read video")
        return

    # Convert to PIL
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)

    print("Processing 1 frame with rembg...")
    start = time.time()
    _ = remove(img)
    end = time.time()
    
    print(f"Time per frame: {end - start:.4f} seconds")
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total video frames: {total_frames}")
    print(f"Estimated total time: {(end - start) * total_frames / 60:.2f} minutes")

    cap.release()

if __name__ == '__main__':
    test_speed()
