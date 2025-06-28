import cv2 as cv
import numpy as np

img = cv.imread("/mnt/c/Users/huyje/Pictures/Entropy.png")
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Display window", img)
img_rgb = cv.resize(img_rgb, (200, 200))
height, width, channel = img_rgb.shape

blur = cv.GaussianBlur(img, (15, 15), 5)
blur2 = cv.GaussianBlur(img, (15, 15), 1)
#cv.imshow("Blur Display", blur2)

synthetic_image = np.array(img_rgb)
for i in range(0, height):
    for j in range(0, width):
        synthetic_image[i, j] = [100, 255, 200]
#cv.imshow("Synthetic Image", synthetic_image)
#cv.imshow("Grey Image", img_grey)

fake_image = np.array([[255, 0, 255], [0, 255, 0], [255, 0, 255]], dtype=np.uint8)
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

# Apply different filters
blurred_avg = cv.blur(fake_image, (5, 5))
blurred_gaussian = cv.GaussianBlur(fake_image, (5, 5), 0)
blurred_median = cv.medianBlur(fake_image, 5)
filtered_custom = cv.filter2D(fake_image, -1, kernel)
filtered_bilateral = cv.bilateralFilter(fake_image, 9, 75, 75)

# Display the results
cv.imshow('Original', fake_image)
cv.imshow('Average Blur', blurred_avg)
cv.imshow('Gaussian Blur', blurred_gaussian)
cv.imshow('Median Blur', blurred_median)
cv.imshow('Custom Filter', filtered_custom)
cv.imshow('Bilateral Filter', filtered_bilateral)


blurred_avg = cv.blur(img_rgb, (3, 3))
#cv.imshow("Blurred Avg", blurred_avg)
k = cv.waitKey(0) # Wait for a keystroke in the window