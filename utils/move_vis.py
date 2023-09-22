import os
import shutil

def is_image_file(filename):
    # Check if the file has a valid image extension
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]
    _, ext = os.path.splitext(filename)
    return ext.lower() in valid_extensions

def move_images_with_prefix(src_folder, dest_folder, prefix):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Get a list of all files in the source folder
    files = os.listdir(src_folder)

    for file in files:
        # Check if the file name starts with the specified prefix and is an image file
        if file.startswith(prefix) and is_image_file(file):
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, file)

            # Move the file to the destination folder
            shutil.move(src_path, dest_path)
            print(f"Moved '{file}' to '{dest_folder}'")

if __name__ == "__main__":
    # Replace 'source_folder_path' with the path to the folder containing the images.
    # Example: source_folder_path = "/path/to/source_folder"
    source_folder_path = "/home/cgv/Personalize-SAM/outputs/persam_f/chicken/"

    # The new folder will be created in the same directory as the source folder.
    dest_folder_path = os.path.join(os.path.dirname(source_folder_path), "vis")

    # Call the function to move the image files with the prefix "vis"
    move_images_with_prefix(source_folder_path, dest_folder_path, "vis")
