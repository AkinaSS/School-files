"""I decide to greyscale the image from lab1 and blur it using GaussianBlur to get the result
I also add in a custom synthetic image made by using np.array() and blur it using both normal and gauss method
Apart from testing and checking the results, problem I have so far is to create synthetic image
making different color for each pixel and to scale the picture to bigger frame or size"""
#Image convolution is a process where you take an image and a filter (or kernel) and apply the filter to the image.
# An edge of a picture is the area where the color scale changes gradually.

import cv2 as cv
import numpy as np

img = cv.imread("/mnt/c/Users/huyje/Pictures/Entropy.png")
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.resize(img_grey, (100, 100))

fake_image = np.array([[255, 0, 255], [0, 255, 0], [255, 0, 255]], dtype=np.uint8)
normal_blur = cv.blur(fake_image, (3, 3))
gaussian_blur = cv.GaussianBlur(fake_image, (3, 3), 0)
cv.imshow("Normal Blur", normal_blur)
cv.imshow("Gaussian Blur", gaussian_blur)

synthetic_image = np.array(img_grey)
blur = cv.GaussianBlur(synthetic_image, (15, 15), 5)
#cv.imshow("Synthetic Image", blur)

cv.waitKey(0) # Wait for a keystroke in the window
cv.destroyAllWindows()