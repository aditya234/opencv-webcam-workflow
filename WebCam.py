import cv2

cap = cv2.VideoCapture(0)
# preprocessing
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)