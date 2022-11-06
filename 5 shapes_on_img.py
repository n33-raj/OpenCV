import cv2
import numpy as np

img = cv2.imread('lena.jpg',1)      ## 0 for gray, 1 for color, -1 for orignal
# img = np.zeros([512,512,4])          ### for black image

### to draw line
img = cv2.line(img,(0,0),(255,255),(0,0,255),3)  ##img, cordinates of x1, y1 & x2, y2, color,thickness
### note: here RGB works in reverse order


### to draw rectangle
img = cv2.rectangle(img,(0,280),(250,380),(255,0,0),5)

#### for filled rectangle
img = cv2.rectangle(img,(350,0),(450,80),(0,0,255),-1)

### text on image
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,3,(255,255,255),2)


img = cv2.circle(img,(255,180),50,(0,255,0),-1)

cv2.imshow('image',img)

cv2.waitKey() 
cv2.destroyAllWindows()