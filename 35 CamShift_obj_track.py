import cv2
import matplotlib.pyplot as plt
import numpy as np

cam = cv2.VideoCapture("slow_traffic.mp4")

### taking first frame of the video
ret, frame = cam.read()

### setup initial location of windows by cv2.selectROI method
x, y, width, height = 530, 135, 78, 37                         
track_window = (x, y, width, height)    

### ROI setup for tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, (0, 60, 32), (180, 255, 255))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

### termination criteria, either 10 iterations or atleast 1
term_crit = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 1)

while True:
    ret, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    ### applying CamShift to get the new location
    ret, track_window = cv2.CamShift(dst, track_window, term_crit)

    ### draw rectangle on image

    x,y,w,h = track_window
    final_image = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),3)

    if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cv2.imshow("final image",final_image)



cam.release()
cv2.destroyAllWindows() 


'''
CamShift is not working properly here need to do hardcode
'''