from PIL import Image

def resize_image(image_path, width, height):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Resize the image
        resized_img = img.resize((width, height))
        
        # Save the resized image
        resized_img.save("D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Player/1F.png")
        print("Image resized successfully.")
    except Exception as e:
        print("Error:", e)

# Path to the image file you want to resize
image_path = "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Player/1.png"

# Dimensions for resizing
new_width = 38
new_height = 53

# Resize the image
resize_image(image_path, new_width, new_height)