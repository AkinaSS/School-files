import cv2 as cv
import numpy as np

jpg_img = cv.imread('./projectGothamRacing/data/onePic.jpg', cv.IMREAD_UNCHANGED)
#png_img = cv.imread('captured_image.png', cv.IMREAD_UNCHANGED)

if jpg_img is None: #or png_img is None:
    print('Error: Could not load!!')
    exit()

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
#cv.imshow('Edge Detection', edges)
cv.imshow('Interesting points', jpg_img)
#cv.imshow("PNG Image", png_img)

cv.waitKey(6000)  # Show it for 6 seconds, then continue
cv.destroyAllWindows()  # Close the image window before opening the webcam

# Open the webcam (0 = default camera)
video_capture = cv.VideoCapture(0)

if not video_capture.isOpened():
    print('Could not open webcam')
    exit()

while True:
    ret, frame = video_capture.read() # .read() captures a frame from the webcam.
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


video_capture.release()
cv.destroyAllWindows()
