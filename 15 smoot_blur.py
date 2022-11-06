from statistics import median
import numpy as np
import cv2
import matplotlib.pyplot  as plt


img = cv2.imread("salt_pepper.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((10,10), np.float32)/100
dst = cv2.filter2D(img,-1, kernal)
blur = cv2.blur(img, (15,15))      ### kernel size must be odd num
gaublur = cv2.GaussianBlur(img,(15,15), 0)
median = cv2.medianBlur(img, 5)

titles = ["image", "dst", "blur", "gaublur", "median"]
images = [img, dst, blur, gaublur, median]


for i in range(5):
    plt.subplot(2,3 , i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
# cv2.waitKey()
# cv2.destroyAllWindows()