import cv2

# Try to access the webcam at /dev/video0
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not access the webcam.")
else:
    print("Webcam opened successfully!")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Webcam Feed", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
