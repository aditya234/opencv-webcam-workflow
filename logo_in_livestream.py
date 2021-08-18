import cv2
import numpy as np


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

logo = cv2.imread('download.png')
size = 100
logo = cv2.resize(logo, (size, size))
grey = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

# masking - take all the color codes which are equal or above 1, and convert them to value 255
_, mask = cv2.threshold(grey, 1, 255, cv2.THRESH_BINARY)

while True:
    _, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    # inserting the logo
    roi = frame[-size - 10:-10, -size - 10:-10]
    roi[np.where(mask)] = 0     # all the places where mask values are non zero, put those as 0 in roi
    roi += logo

    cv2.imshow("Logo in video stream", frame)

    if cv2.waitKey(1) == ord('q'):
        break
