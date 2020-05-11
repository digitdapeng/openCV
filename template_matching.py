# -*- coding: utf-8 -*-
"""

@author: dwang
"""

import cv2
import numpy as np
img = cv2.imread("messi5.jpg")
#548,342
#img = cv2.rectangle(img, (215, 75), (260, 130), (0, 0, 255), 1)
cv2.imshow('image',img)

#faceimg=img[75:130,215:260,:]
#cv2.imshow('Head image',faceimg)
#cv2.imwrite('messi_face.jpg', faceimg)

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("messi_face.jpg", 0)
h,w = template.shape

#res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED )
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED )
print(res)
cv2.imshow('match',res)
threshold = 0.6;
loc = np.where(res >= threshold)
print('loc=:',loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
