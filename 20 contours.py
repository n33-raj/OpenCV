import cv2
import numpy as np
  
image = cv2.imread("opencv-logo2.png")  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

### using canny 
# thresh = cv2.Canny(gray, 50,255)

### using thresholding
ret, thresh = cv2.threshold(gray, 150, 250,0)          ### adjust thrshold value for better results

### CHAIN_APPROX_SIMPLE & CHAIN_APPROX_NONE is two different algorithm for contour detection
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
  
print("Number of Contours found = " + str(len(contours)))
  
### -1 signifies drawing all contours
cv2.drawContours(image, contours, -1, (80, 95, 180), 2)

cv2.imshow('Gray', gray)
cv2.imshow('Contours', image)
cv2.waitKey()
cv2.destroyAllWindows()


### CV_RETR_EXTERNAL: gives "outer" contours
###  CV_RETR_TREE:  calculates the full hierarchy
### using canny is better than thresholding