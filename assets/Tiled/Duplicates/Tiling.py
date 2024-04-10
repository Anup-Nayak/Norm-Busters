from PIL import Image

def combine_images(image_paths):
    # Create a blank canvas to paste images onto
    canvas_width = 0
    canvas_height = 0
    for path in image_paths:
        img = Image.open(path)
        aspect_ratio = img.width / img.height
        if 0.8 <= aspect_ratio <= 1.2:  # Nearly Square
            canvas_width += 180
            canvas_height = max(canvas_height, 180)
        elif 1.8 <= aspect_ratio <= 2.2:  # Nearly Rectangle
            canvas_width += 360
            canvas_height = max(canvas_height, 180)
    
    canvas = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))

    # Paste images onto the canvas
    current_x = 0
    for path in image_paths:
        img = Image.open(path)
        aspect_ratio = img.width / img.height
        print(aspect_ratio)
        if 0.8 <= aspect_ratio <= 1.2:  # Nearly Square
            img = img.resize((180, 180))
        elif 1.8 <= aspect_ratio <= 2.2:  # Nearly Rectangle
            img = img.resize((360, 180))
        canvas.paste(img, (current_x, 0))
        current_x += img.width

    return canvas

if __name__ == "__main__":
    image_paths = ["D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile1.png",
                   "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile2.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile3.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile4.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile5.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile6.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile7.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile8.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile9.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile10.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile11.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile12.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile13.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile14.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile16.png","D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile17.png",
                   "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile18.png",
                   "D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile19.png"
                   ]
    combined_image = combine_images(image_paths)
    combined_image.show()
    combined_image.save("D:/Abhishek_Folder/Coding/Game Dev/COP1/assets/Tiled/Tile1.png/TileMap2.jpg")  # Save the combined image
