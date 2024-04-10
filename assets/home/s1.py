from PIL import Image
import os

print(os.getcwd())

def resize_image(image_path, width, height):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Resize the image
        resized_img = img.resize((width, height))
        
        # Save the resized image
        resized_img.save(os.path.join(os.getcwd(), 'assets/home/home2.png').replace("\\", "/"))
        print("Image resized successfully.")
    except Exception as e:
        print("Error:", e)

# Path to the image file you want to resize
image_path = os.path.join(os.getcwd(), 'assets/home/home.png').replace("\\", "/")

# Dimensions for resizing
new_width = 720
new_height = 1080

# Resize the image
resize_image(image_path, new_width, new_height)