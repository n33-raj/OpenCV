import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("messi5.jpg")
roi = cv2.selectROI("ROI",img)

print(roi)

img_crop = img[int(roi[1]) : int(roi[1]+roi[3]),
            int(roi[0]) : int(roi[0]+roi[2])]

cv2.imshow("cropped image", img_crop)
cv2.waitKey(0)