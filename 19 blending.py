import cv2
import matplotlib.pyplot as plt
import numpy as np


apple = cv2.imread("apple.jpg")
orange = cv2.imread("orange.jpg")

apple_orange = np.hstack((apple[:, :256]    , orange[:, 256: ]))

print(apple.shape)
print(orange.shape)
# print(apple_orange.shape)

down = cv2.pyrDown(apple_orange)


cv2.imshow("Apple", apple)
cv2.imshow("orange", orange)
# cv2.imshow("apple_orange", apple_orange)

cv2.imshow("Pyr Down", down)

cv2.waitKey()
cv2.destroyAllWindows()