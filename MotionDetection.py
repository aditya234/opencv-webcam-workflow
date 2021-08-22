import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

'''
We actually scale down the frame on which we want to do the processing
because processing smaller frames require less amount of processing power
'''
scale = 2
height = 720
width = 1280
last_frame = np.zeros((height//scale, width//scale), np.uint8)

while True:
    # reading, resizing and fliping the frame
    _, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame, 1)

    # processing the frame
    downscaled_frame = cv2.resize(frame,(width//scale, height//scale))
    grey = cv2.cvtColor(downscaled_frame, cv2.COLOR_BGR2GRAY)
    # earlier in motion detection we used gausian filter of 25,25 but now we have scaled our sides by 2
    # hence the filter must reduce by factor of 2*2 ie 4 ie 5,5
    grey = cv2.GaussianBlur(grey, (5, 5), 0)
    # foreground = grey - background
    print(last_frame.shape)
    print(grey.shape)
    # _, mask = cv2.threshold(foreground, 127, 255, cv2.THRESH_BINARY)
    absolute_diff = cv2.absdiff(last_frame, grey)
    last_frame = grey
    _, mask = cv2.threshold(absolute_diff, 15, 255, cv2.THRESH_BINARY)

    # dilated_mask = cv2.dilate(mask,None, iterations = 2)
    contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # means small movement
        if cv2.contourArea(contour) < 250:
            continue
        # means movement detected
        x, y, w, h = cv2.boundingRect(contour)
        # scale the image back up, since its processed
        x, y, w, h = x*scale, y*scale, w*scale, h*scale
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

