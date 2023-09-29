# Imports
import json
import os
import cv2
from skimage.metrics import structural_similarity as ssim

# Folder path
folder_1 = './data1' # Change the folder path
folder_2 = './data2' # Change the folder path

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

# Save json object with the results
def save_json(image1, image2, similarity):
    # Create the json object
    dict = {
        "similarity: " + str(similarity): {
        "folder1": folder_1 + '/' + str(image1),
        "folder2": folder_2 + '/' + str(image2)
        }
    }
    
    return dict

    
    
if __name__ == "__main__":

    images_1 = [] # List of images from folder 1
    images_2 = [] # List of images from folder 2
    label_images_1 = [] # List of labels from folder 1
    label_images_2 = [] # List of labels from folder 2
    json_list = [] # List of json objects

    # Read the images
    read_images(folder_1, folder_2)

    # Compare the images
    for i in range(len(images_1)):
        for j in range(len(images_2)):
            similarity = compare_images(images_1[i], images_2[j])
            if similarity > 0.8: # Minimum similarity
                json_list.append(save_json(label_images_1[i], label_images_2[j], similarity))

    # Save the json file
    out_file = open("results.json", "w")
    json.dump(json_list, out_file, indent=6)
    out_file.close()