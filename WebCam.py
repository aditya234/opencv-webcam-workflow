import cv2

cap = cv2.VideoCapture(0)
# preprocessing
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while True:
    _,frame = cap.read()
    # processing the data / frame
    frame = cv2.resize(frame,(640,480))
    frame = cv2.flip(frame,1)

    # show the frame / data / picture
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1)== ord('q'):
        break