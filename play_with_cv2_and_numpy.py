import cv2
import numpy as np

colorImg = cv2.imread('logo.png')
# colorImg = cv2.resize(colorImg,(50,50))
grey = cv2.cvtColor(colorImg,cv2.COLOR_BGR2GRAY)

roi = grey[3:6,3:6]
roi[:,:] = grey[0:3,0:3]


print(grey)

cv2.imshow("logo",grey)
cv2.waitKey(0)

# _,greyMask = cv2.threshold(grey,1,255,cv2.THRESH_BINARY)
# cv2.imshow("LOGO",greyMask)
# cv2.waitKey(0)

