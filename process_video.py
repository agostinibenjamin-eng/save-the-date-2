import os
import cv2
import imageio
from rembg import remove
from PIL import Image
import numpy as np

def process_video():
    input_video = 'assets/Vidéo_sans_son_personnages_dansants.mp4'
    output_video = 'assets/groupe_mariage_transparent.webm'
    
    cap = cv2.VideoCapture(input_video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0: fps = 30
    
    frames = []
    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"Starting processing for {total_frames} frames...")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        
        # Remove background
        img_no_bg = remove(img)
        
        # Convert back to numpy
        frame_rgba = np.array(img_no_bg)
        frames.append(frame_rgba)
        
        frame_count += 1
        if frame_count % 10 == 0:
            print(f"Processed {frame_count}/{total_frames} frames")
            
    cap.release()
    
    print("Saving video...")
    # Save as WebM with VP9 codec for transparency
    try:
        writer = imageio.get_writer(output_video, fps=fps, codec='libvpx-vp9', pixelformat='yuva420p')
        for frame in frames:
            writer.append_data(frame)
        writer.close()
        print(f"Success! Saved to {output_video}")
    except Exception as e:
        print(f"Error saving video: {e}")
        # Fallback to GIF if WebM fails
        try:
            output_gif = 'assets/groupe_mariage_transparent.gif'
            print(f"Falling back to GIF: {output_gif}")
            imageio.mimsave(output_gif, frames, fps=fps, loop=0)
            print("Saved as GIF")
        except Exception as e2:
            print(f"Error saving GIF: {e2}")

if __name__ == '__main__':
    process_video()
