'''
capture an image stream from your camera and display it, save it to a file. (Same reason like lab 3, camera is not working)
upload an image and display it. What happens if you use a jpg? what happens if you use a .png?
There're currently virtually no difference between jpg and png, the only difference is that jpg is a lossy compression format, while png is lossless.
JPG use 8-bit color depth per channel (RGB), while PNG use transparency via an alpha channel (RGBA).

create filters to detect interesting points: points where there is sufficient variation in intensity that matching should be reliable
iterate through the pixels and print the coordinates of interesting points
write a function to compute the correlation between two points.
write a few sentences on what problems you encountered and answer the following questions
Questions:

what would make a match reliable?
When there's no noise and the pixel intensity is consistent.

If the motion is small, how would you find the best match
From the past project, to find the best match, we can use Shi-Tomasi corner detection and use the detected points to find the best match.
Comparing it along the way

what is a measure of how well two points match?
Intensity of the pixel and how well the corner detection is done.
'''

import cv2 as cv
import numpy as np

jpg_img = cv.imread('./projectGothamRacing/data/onePic.jpg', cv.IMREAD_UNCHANGED)
#png_img = cv.imread('captured_image.png', cv.IMREAD_UNCHANGED)

if jpg_img is None: #or png_img is None:
    print('Error: Could not load!!')
    exit()
    
# Open the webcam (0 = default camera)
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print('Could not open webcam')
    exit()

while True:
    ret, frame = capture.read() # .read() captures a frame from the webcam.
    if not ret:
        print("Error: could not read frame")
        break

    cv.imshow('Webcam Stream', frame) # Display the video stream

    key = cv.waitKey(1) & 0xFF
    if key == ord('s'):  # Press 's' to save the image
        cv.imwrite("captured_image.jpg", frame)
        print("Image saved as captured_image.jpg")
    elif key == ord('q'):  # Press 'q' to exit
        break

# Convert to grayscale
gray = cv.cvtColor(jpg_img, cv.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blurred = cv.GaussianBlur(gray, (5, 5), 1)

# Apply Canny Edge Detection
edges = cv.Canny(blurred, 50, 150)  # Lower and upper thresholds

# Detect interesting points using Shi-Tomasi Corner Detector
corners = cv.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
# Convert float32 values to integers
corners = np.int0(corners)

# Draw circles around detected points
for corner in corners:
    x, y = corner.ravel()
    print(f"({x}, {y})")  # Print coordinates
    cv.circle(jpg_img, (x, y), 10, (0, 255, 0), -1)  # Green circles

# Print image shapes (dimensions)
#print(f"JPG Shape: {jpg_img.shape}")  # (height, width, 3)
#print(f"PNG Shape: {png_img.shape}")  # (height, width, 4) if it has transparency

# Display images
#cv.imshow("JPG Image", jpg_img)
cv.imshow('Edge Detection', edges)
cv.imshow('Interesting points', jpg_img)
#cv.imshow("PNG Image", png_img)

cv.waitKey(6000)  # Show it for 6 seconds, then continue
cv.destroyAllWindows()  # Close the image window before opening the webcam


capture.release()
cv.destroyAllWindows()
