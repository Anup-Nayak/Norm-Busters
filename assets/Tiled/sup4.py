from PIL import Image

def convert_white_to_transparent(image_path):
    # Open the image using PIL
    img = Image.open(image_path)

    # Convert the image to RGBA mode (if not already)
    img = img.convert("RGBA")

    # Get the image data as a list of pixels
    pixel_data = img.getdata()

    # Create a new list to hold the modified pixel data
    new_pixel_data = []

    # Iterate over the pixel data
    for item in pixel_data:
        # If the pixel is white, set its alpha value to 0 (transparent)
        if item[:3] == (255, 255, 255):
            new_pixel_data.append((255, 255, 255, 0))
        else:
            new_pixel_data.append(item)

    # Update the image data with the modified pixel data
    img.putdata(new_pixel_data)

    # Save the modified image
    img.save("D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileMap11.png")

# Example usage
convert_white_to_transparent("D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileMap10.png")
