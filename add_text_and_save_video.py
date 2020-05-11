# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:42:57 2020

@author: dwang
"""

import cv2
import datetime
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

for i in range(100):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

#cap.set(3, 3000)
#cap.set(4, 3000)
#print(cap.get(3))
#print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       font = cv2.FONT_HERSHEY_SIMPLEX
       text = 'Width: '+ str(cap.get(3)) + ' Height:' + str(cap.get(4))
       datet = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
       """
       frame = cv2.putText(frame, text, (10, 50), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
       frame = cv2.putText(frame, datet, (10, 100), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
       """
       frame = cv2.putText(frame, 'Recording...', (10, 40), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
       out.write(frame)
       cv2.imshow('frame', frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()