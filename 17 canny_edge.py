import numpy as np
import cv2
import matplotlib.pyplot  as plt


img = cv2.imread("messi5.jpg", 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

canny = cv2.Canny(img, 100, 200)
canny2 = cv2.Canny(img, 50, 100)
canny3 = cv2.Canny(img, 100, 250)
canny4 = cv2.Canny(img, 10, 200)
canny5 = cv2.Canny(img, 150, 250)



images = [img, canny, canny2, canny3, canny4, canny5]
titles = ["image", "canny", "canny2", "canny3", "canny4", "canny5"]



for i in range(6):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()