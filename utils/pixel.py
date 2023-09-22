from PIL import Image

def convert_pixels(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert("RGB")  # Convert to RGB mode to ensure consistent behavior
    except IOError:
        print(f"Error: Cannot open the image at '{image_path}'.")
        return

    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y] == (255, 255, 255):
                print('e')
                pixels[x, y] = (128, 0, 0)

    # Save the modified image
    image.save(image_path)  # Replace with the desired output file name

if __name__ == "__main__":
    image_path = "/home/cgv/Personalize-SAM/data/TestAnnotations/pizza2/000.png"  # Replace with the actual path to your image
    convert_pixels(image_path)