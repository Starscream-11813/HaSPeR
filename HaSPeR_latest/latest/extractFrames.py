# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
vid = cv2.VideoCapture("./EditedVideos/Snail.mp4")

try:

    # creating a folder named data
    if not os.path.exists('snailFrames'):
        os.makedirs('snailFrames')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0
id = 0

while (True):

    # reading from frame
    success, frame = vid.read()

    if success:
        if currentframe % 7 == 0:
# continue creating images until video remains
            name = './snailFrames/snail_' + str(id) + '.PNG'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)
            id += 1

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
vid.release()
cv2.destroyAllWindows()