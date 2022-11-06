### *************************** MERGING ONE PIC WITH OTHER ******************************


import cv2
import numpy as np

img = cv2.imread("messi5.jpg")
img2 = cv2.imread("opencv-logo.png")

### size must be same if we add two images
img = cv2.resize(img,(480,512))
img2 = cv2.resize(img2,(480,512))

### addweighted method
merged_img = cv2.addWeighted(img,0.9, img2,0.3, 0)        ## 0.9 & 0.3 are the percentage to visibility of images

## adding both images
# merged_img = cv2.add(img, img2)


cv2.imshow("image",merged_img)
cv2.waitKey(0) & 0xFF == ord("x")
cv2.destroyAllWindows()