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
        resized_img.save(os.path.join(os.getcwd(),'spikef.png').replace("\\", "/"))
        print("Image resized successfully.")
    except Exception as e:
        print("Error:", e)

image_path = os.path.join(os.getcwd(), 'spikef.png').replace("\\", "/")

new_width = 180
new_height = 180
# Resize the image
resize_image(image_path, new_width, new_height)
