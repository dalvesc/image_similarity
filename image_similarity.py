# Imports
import os
import cv2
from skimage.metrics import structural_similarity as ssim
import skimage

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
            label_images_1.append(filename)

    for filename in os.listdir(folder_2):
        img = cv2.imread(os.path.join(folder_2,filename)) # Read the image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
        img = cv2.resize(img, (224, 224)) # Resize the image
        if img is not None:
            images_2.append(img)
            label_images_2.append(filename)

# Return the similarity between two images
def compare_images(imageA, imageB):
    # Compute the structural similarity index for the images
    s = ssim(imageA, imageB) # Valor 1 = 100% similarity
    
    return s

# Save json file with the results
def save_json(image1, image2):
    # Create the json file
    json_file = open("./results.json", "a")
    # Write the results
    json_file.write("{\n")
    json_file.write("folder_1\t\"image1\": \"" + str(image1) + "\",\n")
    json_file.write("folder_2\t\"image2\": \"" + str(image2) + "\",\n")
    json_file.write("},\n")
    # Close the json file
    json_file.close()

    
    
if __name__ == "__main__":

    images_1 = []
    images_2 = []
    label_images_1 = []
    label_images_2 = []

    # Read the images
    read_images(folder_1, folder_2)

    # Compare the images
    for i in range(len(images_1)):
        for j in range(len(images_2)):
            similarity = compare_images(images_1[i], images_2[j])
            if similarity > 0.8: # Minimum similarity
                save_json(label_images_1[i], label_images_2[j])