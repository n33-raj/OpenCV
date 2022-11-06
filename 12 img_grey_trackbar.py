import cv2
import numpy as np

cv2.namedWindow("image")
def nothing(x):
    print(nothing)

cv2.createTrackbar( "color/gray", "image", 0, 1, nothing)

while True:
        img = cv2.imread('lena.jpg')

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        s = cv2.getTrackbarPos( "color/gray", "image")
        if s==0:
            pass
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = cv2.imshow("image", img)

cv2.destroyAllWindows()