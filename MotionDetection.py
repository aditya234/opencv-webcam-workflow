import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

# iterating lets camera have the timet to adjust to the lightening and aspect ratios
for _ in range(10):
    _, background = cap.read()
background = cv2.resize(background, (1280, 720))
background = cv2.flip(background, 1)
background = cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
last_frame = cv2.GaussianBlur(background,(25,25),0)

while True:
    # reading, resizing and fliping the frame
    _, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame,1)

    # processing the frame
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (25, 25), 0)
    # foreground = grey - background

    # _, mask = cv2.threshold(foreground, 127, 255, cv2.THRESH_BINARY)
    absolute_diff = cv2.absdiff(last_frame,grey)
    last_frame = grey
    _, mask = cv2.threshold(absolute_diff, 15, 255, cv2.THRESH_BINARY)

    # dilated_mask = cv2.dilate(mask,None, iterations = 2)
    contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # means small movement
        if cv2.contourArea(contour) < 2000:
            continue
        # means movement detected
        x, y, width, height = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+width, y+height),(0,255,0),2)
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

