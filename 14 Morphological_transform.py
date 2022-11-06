import numpy as np
import cv2
import matplotlib.pyplot  as plt


img = cv2.imread("smarties.png", 0)
ret,mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)   ### thershold takes two variables like a,b

kernal = np.ones((2,2), np.uint8)/4

dilation = cv2.dilate(mask, kernal, iterations=4)        ### to remove white noise
erosion = cv2.erode(mask, kernal, iterations=8)
open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

titles = ["image", "mask", "dilation", "erosion", "open", "close"]
images = [img, mask, dilation, erosion, open, close]


for i in range(6):
    plt.subplot(2, 3 , i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.show()
# cv2.waitKey()
# cv2.destroyAllWindows()