#Group: Torsten, Duc, Cleo

import cv2 as cv
import numpy as np
import os
import matplotlib 
import random as rd
import gc
import dask
from dask import delayed, compute
from compare import homography, bruteForce, knnBruteForce, Flann


matplotlib.use('TkAgg')

folder_path = "./data/image_and_xml/images"
# Specify the chunk size (how many images to process at a time)
chunk_size = 1000

# List all image files in the folder (filter by extensions)
all_images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Number of chunks
num_chunks = len(all_images) // chunk_size + (1 if len(all_images) % chunk_size > 0 else 0)

# List of images
default_list = np.empty(len(all_images), dtype=object)

def process_image(filename):
    img_path = os.path.join(folder_path, filename)
    img = cv.imread(img_path)
    
    if img is not None:
        # Process image here (you can add any operations like resizing, filtering, etc.)
        print(f"Processing image: {filename}")
        img = cv.resize(img, (500, 500))
        return img
    else:
        print(f"Could not load image: {filename}")
        return None

#Loop through chunks of images
for chunk_index in range(num_chunks):
    print(f"Processing chunk {chunk_index + 1} of {num_chunks}...")
    
    # Get the start and end indices for the current chunk
    start_idx = chunk_index * chunk_size
    end_idx = start_idx + chunk_size
    current_chunk = all_images[start_idx:end_idx]
    
    # Use Dask to process images in parallel
    tasks = [delayed(process_image)(filename) for filename in current_chunk]
    results = compute(*tasks)
        
    default_list = np.append(default_list, [img for img in results if img is not None])
        
    print(len(default_list))
    
    # Clear memory
    del current_chunk
    gc.collect()
    
# Convert the list of images to a NumPy array
images_array = np.array(default_list)

if __name__ == "__main__": 
    while True:
        # Randomly select 2 images from the list 
        random_images = rd.sample(images_array, 2)
        userInput = input('Choose an option: \n 1. Brute Force \n 2. KNN Brute Force \n 3. FLANN \n 4. Homography \n 5. Credits\nq. Quit \n')
        random_img1 = os.path.join(folder_path, random_images[0])
        random_img2 = os.path.join(folder_path, random_images[1])
        if userInput == '1':
            bruteForce(random_img1, random_img2)        
        elif userInput == '2':
            knnBruteForce(random_img1, random_img2)
        elif userInput == '3':
            Flann(random_img1, random_img2)
        elif userInput == '4':
            homography(random_img1, random_img2)
        elif userInput == '5':
            print('Credits: \n Torsten, Duc, Cleo \n')
        elif userInput == 'q':
            print('Exiting...')
            break
        else:
            print('Only 1, 2, 3, 4, or 5 you donut!')
            break

        cv.waitKey(0)
        cv.destroyAllWindows()