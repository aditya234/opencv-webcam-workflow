import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

back_sub = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = cap.read()

    fg_mask = back_sub.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("FG Mask", fg_mask)

    if cv2.waitKey(1) == ord('q'):
        break