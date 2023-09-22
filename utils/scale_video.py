import cv2

def scale_video(input_video_path, output_video_path, scale_factor=0.25):
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error opening video file.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Get the video codec of the input video
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

    # Set the output video codec options
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (new_width, new_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        frame = cv2.resize(frame, (new_width, new_height))

        # Write the resized frame to the output video
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Video scaling completed successfully.")

if __name__ == "__main__":
    input_video = "/home/cgv/Personalize-SAM/outputs/video/persam_f/pizza2.mp4"
    output_video = "/home/cgv/Personalize-SAM/outputs/videonew/persam_f/pizza2.mp4"
    scale_factor = 0.25
    scale_video(input_video, output_video, scale_factor)
