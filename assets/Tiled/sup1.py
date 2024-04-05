from PIL import Image

def add_images(main_image_path, small_image_paths, start_x, start_y):
    main_image = Image.open(main_image_path)
    main_width, main_height = main_image.size
    
    # Ensure the main image is 1080x1080
    if main_width != 1080 or main_height != 1080:
        print("Main image should be 1080x1080.")
        return None
    
    # Check if there are enough small images
    if len(small_image_paths) < 4:
        print("There should be at least 5 small images.")
        return None
    
    # Open small images, resize, and paste onto main image
    for i, small_image_path in enumerate(small_image_paths):
        if i < 5:
            small_image = Image.open(small_image_path)
            small_image = small_image.resize((180, 180))
            main_image.paste(small_image, (start_x, start_y))
            start_x += 180
    
    return main_image

if __name__ == "__main__":
    main_image_path = "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/output_image_without_gray.png"
    small_image_paths = ["D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileBoundaryF1.png", "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileBoundaryF2.png", "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileBoundaryF3.png", "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/TileBoundaryF4.png", ]  # Paths to small images
    start_x = 0
    start_y = 180
    
    combined_image = add_images(main_image_path, small_image_paths, start_x, start_y)
    if combined_image:
        combined_image.show()
        combined_image.save("D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/combined_image.png")
