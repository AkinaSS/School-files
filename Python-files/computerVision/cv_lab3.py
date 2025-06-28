'''
capture an image from your camera and display it (currently not working,
I've been digging around for solutions to fix, including installing WSL's usbipd and usbip and attach the webcam,
for a whole week and can't find it, the only solution so far is either have an external video capture device
plug in to one of the usb or running the code on a machine that's running a Linux distro)
/Edit: Actually, running the code straight on windows itself or use a virtual camera software like OBS might work

upload an image and display it
create a synthetic image with a checkerboard  
iterate through the pixels and print some of the values
iterate through an image and modify the pixels: use a threshold to set values to 0 or 255
iterate through an RGB image and enhance the Red channel

write a few sentences on what problems you encountered and answer the following questions
Outside of the camera issue, I have no problem with the code, since most is based from the last lab

Questions:

what is the type of an image in OpenCV-Python
In the case of the synthetic image, it is a numpy array of uint8 type

What is the shape of the array?
The shape of the array is (3, 3) for the synthetic image
For normal image, it is (height, width)

What is an edge at a pixel?
It's the boundary or transition point between pixels with different intensities or colors
For example one of the pixel along the line has a value of 255, while the other has a value of 0
'''

import cv2 
import numpy as np 

# python -m venv venv
# venv/Scripts/activate.bat
# pip install opencv-python
# python main.py

# https://github.com/opencv/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# capture frames from a camera 
cap = cv2.VideoCapture(0) 
  
# loop runs if capturing has been initialized. 
while True:  
  
    # reads frames from a camera 
    ret, img = cap.read()  
  
    # convert to gray scale of each frames 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
  
    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 

        # Detects Eyes
        eyes = face_cascade.detectMultiScale(roi_gray)  
    
        #To draw a rectangle in eyes 
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
            
        # Detects Eyes
        smiles = face_cascade.detectMultiScale(roi_gray)  
    
        #To draw a rectangle in eyes 
        for (ex,ey,ew,eh) in smiles: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,255),2) 

    # Display an image in a window 
    cv2.imshow('img',img) 
  
    # Stop if Escape or Exit button is pressed
    if cv2.waitKey(30) == 27 or cv2.getWindowProperty('img', 0) == -1: 
        break
  
onePic = cv2.imread('./projectGothamRacing/onePic.jpg')
brick_cascade = cv2.CascadeClassifier('./projectGothamRacing/onePic.xml')
cv2.imshow('onePic', onePic)

for y in range(onePic.shape[0]):  # Height (rows)
    for x in range(onePic.shape[1]):  # Width (columns)
        # Access the pixel value
        pixel = onePic[y, x]
        
        # If the image is in color (BGR format), pixel will be a tuple (B, G, R)
        blue, green, red = pixel
        red = 255 if red > 127 else 0
        onePic[y, x] = [blue, green, red]

        print(f"Pixel at ({x}, {y}): B={blue}, G={green}, R={red}")

        onePic[y, x] = [255, 255, 255]
        print(f"Pixel at ({x}, {y}): B={blue}, G={green}, R={red}")

fake_image = np.array([[255, 0, 255], [0, 255, 0], [255, 0, 255]], dtype=np.uint8)
for i in range(fake_image.shape[0]):
    for j in range(fake_image.shape[1]):
        print(fake_image[i][j])
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  
