import os
import cv2

def resize_image(image, new_height):
    height, width, _ = image.shape
    new_width = int(width * (new_height / height))
    return cv2.resize(image, (new_width, new_height))

def images_to_video(image_folders, output_video_path, duration_per_frame=2):
    num_folders = len(image_folders)
    image_files = [sorted([f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]) for folder in image_folders]
    
    if not all(image_files):
        print("Image files not found in one or more folders.")
        return
    
    num_images_per_folder = [len(files) for files in image_files]
    
    if len(set(num_images_per_folder)) != 1:
        print("All folders must contain the same number of image files.")
        return
    
    frame_rate = 1 / duration_per_frame
    images = [cv2.imread(os.path.join(image_folders[i], image_files[i][0])) for i in range(num_folders)]
    max_height = max(image.shape[0] for image in images)
    images = [resize_image(image, max_height) for image in images]
    total_width = sum(image.shape[1] for image in images)
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (total_width, max_height))

    for img_set in zip(*image_files):
        frame_images = []
        for i, img_name in enumerate(img_set):
            image = cv2.imread(os.path.join(image_folders[i], img_name))
            image = resize_image(image, max_height)
            frame_images.append(image)
        
        combined_frame = cv2.hconcat(frame_images)

        for _ in range(int(duration_per_frame * frame_rate)):
            video_writer.write(combined_frame)

    video_writer.release()
    print("Video creation completed successfully.")

if __name__ == "__main__":
    script_name = "persam_f/"
    img_cat_name = "pizza2"
    image_folders = [
        "/home/cgv/Personalize-SAM/outputs/" + script_name + img_cat_name + "/bad", 
        "/home/cgv/Personalize-SAM/outputs/" + script_name + img_cat_name + "/vis/bad", 
        ]
    output_video = "/home/cgv/Personalize-SAM/outputs/video/" + script_name + img_cat_name + ".mp4"
    images_to_video(image_folders, output_video)
