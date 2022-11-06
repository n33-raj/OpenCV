import numpy as np
import cv2
import matplotlib.pyplot  as plt


img = cv2.imread("messi5.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1)
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelx = np.uint8(np.absolute(sobelx))

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobely = np.uint8(np.absolute(sobely))


titles = ["image", "laplacian", "sobelx", "sobely"]
images = [img, lap, sobelx, sobely ]


for i in range(4):
    plt.subplot(2,2 , i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()