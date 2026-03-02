import cv2

# Load the video
video = cv2.VideoCapture("lecture6/JW2.mp4")
success, frame = video.read()
count = 0

while success:
    # Save each frame as a JPG
    cv2.imwrite(f'frame{count}.jpg', frame)
    success, frame = video.read()
    count += 1

video.release() # Release resources [9]



# import os , shutil


# cc = os.path.curdir

# gg = os.listdir(cc)

# for file in gg:
#     if file.endswith(".jpg"):
#      shutil.move(src=file, dst="/home/nba-young-boy/Documents/openlabsschool/Gryffindor/Newton/lecture6/Assignment_files")