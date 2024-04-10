from PIL import Image

# Open the PNG file
image = Image.open("D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileMap7.PNG")

# Check if the image has an alpha channel
if image.mode == 'RGBA':
    print("Image has an alpha channel (supports transparency).")
else:
    print("Image does not have an alpha channel.")
