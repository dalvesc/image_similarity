# Imports
import os
import cv2
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np


# Folder path
folder_1 = '' # Change the folder path
folder_2 = '' # Change the folder path

# Read the images and store them in a list
def read_images(folder_1, folder_2):
    for filename in os.listdir(folder_1):
        img = cv2.imread(os.path.join(folder_1,filename)) # Read the image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
        img = cv2.resize(img, (224, 224)) # Resize the image
        if img is not None:
            images_1.append(img)

    for filename in os.listdir(folder_2):
        img = cv2.imread(os.path.join(folder_2,filename)) # Read the image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
        img = cv2.resize(img, (224, 224)) # Resize the image
        if img is not None:
            images_2.append(img)

# Return the similarity between two images
def compare_images(imageA, imageB):
    # Compute the structural similarity index for the images
    s = ssim(imageA, imageB) # Max valor, more similar
    
    return s

