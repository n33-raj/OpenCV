import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("shapes.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127,255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for i in contours:
    ### all shapes are closed so True, arcLength calculate contour parameter, curve length
    ### approxPolyDP : To perform an approximation of a shape of a contour
    approx = cv2.approxPolyDP(i, 0.01*cv2.arcLength(i, True), True)
    cv2.drawContours(img, [approx], 0, (255,0,0), 3)

    x = approx.ravel()[0]      ### ravel: for flatten aray
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1 , (0,255,0), 2)
    
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        ratio = w/h
        print(ratio)
        if 0.95<ratio<1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2) 

    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)


plt.imshow(img)
plt.show()