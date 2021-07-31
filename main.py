import cv2
import time

# Get the webcam
cap = cv2.VideoCapture(0)

# Need a time before we enter the while-loop
last_time = time.time()
# Loop forever (or until break)
while True:
    # Read the a frame from webcam
    _, frame = cap.read()
    # Resize the frame
    frame = cv2.resize(frame, (640, 480))
    # Flip the frame
    frame = cv2.flip(frame, 1)

    # Adding the Frames-per-second
    text = "FPS: " + str(int(1 / (time.time() - last_time)))
    last_time = time.time()
    # Add the text to the frame
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # Show the frame in a window
    cv2.imshow('WebCam', frame)

    # Check if q has been pressed to quit
    if cv2.waitKey(1) == ord('q'):
        break