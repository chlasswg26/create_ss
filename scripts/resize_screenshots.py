from PIL import Image
import os

# Define required sizes
sizes = {
    "6.7_portrait": (1290, 2796),
    "6.7_landscape": (2796, 1290),
    "6.9_portrait": (1320, 2868),
    "6.9_landscape": (2868, 1320),
}

# Input and output directories
input_dir = 'screenshots/original'
output_dir = 'screenshots/resized'

# Create output directories
for size_key in sizes.keys():
    os.makedirs(os.path.join(output_dir, size_key), exist_ok=True)

# Resize images
for filename in os.listdir(input_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        for size_key, size in sizes.items():
            resized_img = img.resize(size, Image.LANCZOS)  # Use LANCZOS for high-quality resizing
            resized_img.save(os.path.join(output_dir, size_key, filename))

print("Resizing complete.")