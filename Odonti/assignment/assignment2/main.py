

import cv2
import os

def extract_frames(video_path, output_folder="frames"):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    frame_count = 0
    print(f"Starting frame extraction from {video_path}...")

    while True:
        # Read a new frame
        ret, frame = cap.read()

        # If the frame was not read successfully, the video has ended
        if not ret:
            break

        # Save the frame as an image file (using zero-padding for correct sorting)
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        print(f"Saved frame {frame_count} as {frame_filename}")
        frame_count += 1

    # Release the video capture object and close all windows
    cap.release()
    print(f"Video processing finished. Total frames extracted: {frame_count}")

# Example usage:
# Replace 'your_video.mp4' with the path to your video file
video_file = 'basketball.mp4'
extract_frames(video_file, output_folder='extracted_frames')

