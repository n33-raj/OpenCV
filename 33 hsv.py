import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("tony.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("image", img)
# cv2.waitKey()

cv2.imshow("hsv", hsv)
cv2.waitKey()
cv2.destroyAllWindows()