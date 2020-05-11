# -*- coding: utf-8 -*-
"""

@author: dwang
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
#img = np.zeros((200,200), np.uint8)
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
#b, g, r = cv2.split(img)
#cv2.imshow("img", img)
#cv2.imshow("b", b)
#cv2.imshow("g", g)
#cv2.imshow("r", r)

#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
import imutils

def histogram_contours(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    plt.imshow(hist, interpolation="nearest")
    plt.show()

    # shape
    lower = np.array([230, 230, 230])
    upper = np.array([255, 255, 255])
    shapeMask = cv2.inRange(img, lower, upper)

    # find the contours in the mask
    cnts = cv2.findContours(
        shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    print("I found {} white shapes".format(len(cnts)))
    cv2.imshow("Mask", shapeMask)

    # loop over the contours
    for c in cnts:
        # draw the contour and show it
        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(0) 
"""        
#histogram_contours(img)