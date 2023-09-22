import os

def rename_images(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    image_files = [filename for filename in os.listdir(folder_path) if filename.endswith((".jpg", ".jpeg", ".png", ".gif"))]

    # Sort the image files alphabetically (based on the original filenames)
    image_files.sort()

    for idx, filename in enumerate(image_files):
        # Generate the new filename with three digits format
        new_filename = '%03d' % (idx) + os.path.splitext(filename)[1]
        # Join the folder path with the new filename
        new_filepath = os.path.join(folder_path, new_filename)
        # Rename the file
        os.rename(os.path.join(folder_path, filename), new_filepath)

if __name__ == "__main__":
    folder_path = "/home/cgv/Personalize-SAM/data/TestImages/banana"  # Replace with the actual path to your folder
    rename_images(folder_path)
