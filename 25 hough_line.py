"""
1) The Hough Transform is a method that is used in image processing to detect any shape,
if that shape can be represented in mathematical form. It can detect the shape even if it is broken or distorted a little bit. 

2) A line can be represented as y = mx + c or in polar coordinates as r(roh) = xcosθ + ysinθ.
(where r is the perpendicular distance from origin to the line, and θ is the angle formed by this perpendicular line)
in hough line detection we use m,c cordinates instead of x,y cordinates,
so, y = mx + c
can be written as, c = y - mx

r(roh) = xcosθ + ysinθ
as, y = -cosθ/sinθ * x  + r/sinθ           and cordinates will be r, θ  


there are two types of Hough Line transforms:
                                 1) standrad hough line transform   (HoughLines)
                                 2) probalistic hough line transform (HoughLinesP)



steps:
    1) edge detection e.g. canny edge detection
    2) mapping of edge point to hough space
    3) interpretation by thresholding
    4) conversion of infinite lines to finite lines

"""

import cv2
import numpy as np

img = cv2.imread("road.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
'''linss = cv2.HoughLines(image, rho, theta, threshold)
theta = angle in radian,  threshold = maximum threshold value,  rho = distance from the cordinates '''

for i in lines:
    rho, theta = i[0]
    a = np.cos(theta)
    b = np.sin(theta)


    x0 = a * rho               ### x0 stores the value rcos(theta)
    y0 = b * rho               ### y0 stores the value rsin(theta)
 
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))

    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 2)


cv2.imshow("image", img)
cv2.imshow("canny", gray)
cv2.waitKey()
cv2.destroyAllWindows()