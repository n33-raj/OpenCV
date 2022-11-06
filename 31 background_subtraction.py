'''
Background Subtraction can also be used as visitor counter.
there are several algorithms used in background subtraction.

OpenCV provides us 3 types of Background Subtraction algorithms:-

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()     - without shadow
fgbg = cv2.createBackgroundSubtractorMOG2()        - with shadown
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture("traffic.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
while cap.isOpened():
    ret, frame = cap.read()

    ## applying on each frame
    fgmask = fgbg.apply(frame)


    if cv2.waitKey(20) & 0xFF == ord("q"):
        break


    cv2.imshow("frame", fgmask)

cap.release()
cv2.destroyAllWindows()