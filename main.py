# env: opencv39
from modules.crop_image import crop_image
from modules.load_images_from_folder import load_images_from_folder, get_image_paths
from PIL import Image
import PIL
import sys
import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
from modules.open_dialog import open_image_dialog, open_mp4_dialog

# Here are some version combinations which the app is tested on (and work)
print("OpenCV2: " + cv2.__version__)  # 4.9.0  / 4.10.0
print("python: " + sys.version[0:7])  # 3.9.18 / 3.12.4
print("NumPy: " + np.__version__)     # 1.26.1 / 1.26.4
print("PIL: " + PIL.__version__)      # 9.5.0  / 10.3.0

TEMPLATE_IMG_PATH = open_image_dialog()
TEMPLATE_IMG = Image.open(TEMPLATE_IMG_PATH)
TEMPLATE_VIDEO = open_mp4_dialog()
MINIMUM_ACCURACY = 0.90
FRAME_SKIP = 210
video_name = os.path.basename(TEMPLATE_VIDEO)
SAVE_LOC = f"./results/{video_name[:-4]}/"


def seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, remaining_seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(remaining_seconds)

# try to create save folder
try:
    if not os.path.exists(SAVE_LOC):
        os.makedirs(SAVE_LOC)
except OSError:
    print('Error: Creating directory of data')

# variables

cam = cv2.VideoCapture(TEMPLATE_VIDEO) # Load Video
total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))

currentframe = 0


while (True):

    # read next frame
    ret, frame = cam.read()
    
    # check if there is a next frame
    try:
        video_frame = frame.copy()
    except:
        print('breaking')
        break

    # every x frames try to match template
    if currentframe % FRAME_SKIP == 0: # 240
        # load template img
        template = cv2.imread(TEMPLATE_IMG_PATH, 0)
        
        # greyscale the img
        video_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
        
        # match the template
        result = cv2.matchTemplate(video_frame, template, cv2.TM_CCOEFF_NORMED)
        
        # break down the results
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        # print the frame
        print(f"frame {currentframe}/{total_frames}: {max_val}")
        
        # if good match save img
        if (max_val)>MINIMUM_ACCURACY:
            # save img
            seconds = currentframe*0.0333333333333333333
            hours, minutes, seconds = seconds_to_hms(seconds)

            file_name = f"{SAVE_LOC}time_{hours}_{minutes}_{seconds}.jpg"
            cv2.imwrite(file_name, frame)

    currentframe+=1


# Release all space and windows once done
cam.release()