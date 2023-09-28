# Read the folders
import os
import cv2

# Folder path
folder_1 = '' # Change the folder path
folder_2 = '' # Change the folder path

# Read the images and store them in a list
images_1 = []

for filename in os.listdir(folder_1):
    img = cv2.imread(os.path.join(folder_1,filename))
    if img is not None:
        images_1.append(img)

images_2 = []

for filename in os.listdir(folder_2):
    img = cv2.imread(os.path.join(folder_2,filename))
    if img is not None:
        images_2.append(img)

