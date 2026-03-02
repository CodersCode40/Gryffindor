import cv2
from os import path

# Load the video

file = path.join("files", "activate.mp4")

video = cv2.VideoCapture(file)
success, frame = video.read()
count = 0

while success:
    # Save each frame as a JPG
    cv2.imwrite(f'./files/Videotoframe{count}.jpg', frame)
    success, frame = video.read()
    count += 1

video.release() # Release resources 



