from PIL import Image

# Open an image file
image = Image.open("D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileMap7.png")

# Resize the image to a new width and height
new_width = 150	
new_height = 150
resized_image = image.resize((new_width, new_height))

# Save the resized image
resized_image.save("D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileMap9.png")

