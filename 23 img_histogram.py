''' Image histogram shows that how many pixles from a particular section of image belongs to 0-255'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena.jpg") 
cv2.imshow("Image", img)

print(img.shape)


plt.hist(img.ravel(), 255, [0, 255])



plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()