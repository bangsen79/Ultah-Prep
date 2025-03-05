from PIL import Image
import os

def crop_to_aspect(image, aspect_ratio):
    img_width, img_height = image.size
    target_width, target_height = aspect_ratio

    # Calculate the target aspect ratio and the image's aspect ratio
    target_ratio = target_width / target_height
    img_ratio = img_width / img_height

    if img_ratio > target_ratio:
        # Image is wider than needed, crop the width
        new_width = int(target_ratio * img_height)
        offset = (img_width - new_width) // 2
        cropped_img = image.crop((offset, 0, offset + new_width, img_height))
    else:
        # Image is taller than needed, crop the height
        new_height = int(img_width / target_ratio)
        offset = (img_height - new_height) // 2
        cropped_img = image.crop((0, offset, img_width, offset + new_height))
    return cropped_img

# Use the current directory where the script is running
directory = os.getcwd()

# Desired aspect ratio (width, height)
aspect_ratio = (3213, 5712)

# Desired final size
desired_size = (3213, 5712)  # Adjust this as needed for the final display size

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".heic"):
        # Open the image file
        with Image.open(os.path.join(directory, filename)) as img:
            # Crop the image to the desired aspect ratio
            cropped_img = crop_to_aspect(img, aspect_ratio)
            # Resize the cropped image
            img_resized = cropped_img.resize(desired_size, Image.Resampling.LANCZOS)
            
            # Save the resized image back to the directory with a new name
            img_resized.save(os.path.join(directory, f"resized_{filename}"))

print("All selected images have been resized and cropped.")
