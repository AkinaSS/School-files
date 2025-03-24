#Group: Torsten, Duc, Cleo

import cv2 as cv
import numpy as np
import os
import matplotlib 
import random as rd
import sys
from compare import homography, bruteForce, knnBruteForce, Flann

matplotlib.use('TkAgg')

folder_path = "./data/image_and_xml/images"

# List all image files in the folder (filter by extensions)
all_images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

def load_and_validate_image(img_path):
    img = cv.imread(img_path)
    if img is not None and isinstance(img, np.ndarray):
        return img
    else:
        print(f"Could not load or invalid image: {img_path}")
        return None

if __name__ == "__main__": 
    while True:
        userInput = input('Choose an option: \n 1. Brute Force \n 2. KNN Brute Force \n 3. FLANN \n 4. Homography \n 5. Credits\nq. Quit \n')
        # Randomly select 2 images from the list 
        random_images = rd.sample(all_images, 2)
        # Read and validate the selected random images
        random_images_paths = [os.path.join(folder_path, filename) for filename in random_images]
        valid_images = [load_and_validate_image(img_path) for img_path in random_images_paths]
        for img in valid_images:
            if img is None:
                print('Invalid images, retrying...')
                break
        random_img1, random_img2 = random_images_paths
        
        if sys.version_info[1] < 12:
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
                print('WHERE\'S THE LAMB SAUCE?!')
                print('WHERE\'S THE LAMB SAUCCEEEEEEEEEEEEEE?!')
                break
        elif sys.version_info[1] >= 12:
            match userInput:
                case 1:
                    bruteForce(random_img1, random_img2)
                case 2:
                    knnBruteForce(random_img1, random_img2)
                case 3:
                    Flann(random_img1, random_img2)
                case 4:
                    homography(random_img1, random_img2)
                case 5:
                    print('Credits: \n Torsten, Duc, Cleo \n')
                case 'q':
                    print('Exiting...')
                    break
                case _:
                    print('WHERE\'S THE LAMB SAUCE?!')
                    print('WHERE\'S THE LAMB SAUCCEEEEEEEEEEEEEE?!')
                    break

        cv.waitKey(0)
        cv.destroyAllWindows()