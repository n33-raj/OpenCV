import cv2
import numpy as np

# img = np.zeros([512,512,3])
img = cv2.imread('lena.jpg')
points= []


def mouse_click(event, x, y, flag, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0,0,255), -1)
        points.append((x, y))
        if len(points) >= 2:            ### if there are two or more thn two circles then it will connect through a line
            cv2.line(img, points[-1], points[-2], (0,0,255), 2)     ### points[-1] means we joining the last element


        cv2.imshow('image',img)

cv2.imshow('image',img)

cv2.setMouseCallback('image',mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()