import os
from rembg import remove
from PIL import Image

def process_images():
    assets_dir = 'assets'
    output_dir = 'assets'
    
    # List all image files
    extensions = ('.png', '.jpg', '.jpeg')
    files = [f for f in os.listdir(assets_dir) if f.lower().endswith(extensions) and 'groupe' not in f and 'cutout' not in f]
    
    for filename in files:
        input_path = os.path.join(assets_dir, filename)
        fname_no_ext = os.path.splitext(filename)[0]
        output_filename = f"{fname_no_ext}_cutout.png"
        output_path = os.path.join(output_dir, output_filename)
        
        print(f"Processing {filename}...")
        
        try:
            input_image = Image.open(input_path)
            output_image = remove(input_image)
            output_image.save(output_path)
            print(f"Saved to {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == '__main__':
    process_images()
