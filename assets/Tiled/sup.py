from PIL import Image

def erase_gray_pixels(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert image to RGBA mode if it's not already
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    # Get the dimensions of the image
    width, height = image.size
    
    # Create a blank image with the same dimensions and mode as the original image
    erased_image = Image.new(mode='RGBA', size=(width, height), color=(255, 255, 255, 0))
    
    # Iterate through each pixel in the original image
    for x in range(width):
        for y in range(height):
            # Get the pixel value
            pixel = image.getpixel((x, y))
            
            # Check if the pixel is grayscale (r = g = b)
            if pixel[0] == pixel[1] == pixel[2] and (pixel[0] > 5):
                # If the pixel is grayscale, set its alpha value to 0 (transparent)
                erased_image.putpixel((x, y), (pixel[0], pixel[1], pixel[2], 0))
            else:
                # If the pixel is not grayscale, copy it to the new image
                erased_image.putpixel((x, y), pixel)
    
    # Save the modified image
    erased_image.save(output_path)
    print("Grayscale pixels erased successfully!")


# Example usage:
input_image_path = "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileMap4.png"  # Change this to the path of your input image
# input_image_path.show()
output_image_path = "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileMap5.png"  # Change this to the desired output path
erase_gray_pixels(input_image_path, output_image_path)
