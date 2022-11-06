import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("lena.jpg")
# img2 = cv2.pyrDown(img)

layer = img.copy()

for i in range(0,3):
    layer = cv2.pyrDown(layer) 
    cv2.imshow(str(i), layer)

cv2.imshow("origina Image", img)
cv2.waitKey()
cv2.destroyAllWindows()