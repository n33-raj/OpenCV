import numpy as np
import cv2


img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255, 255, 255), -1)

img2 = np.full((250,500,3), 255, dtype=np.uint8)
img2 = cv2.rectangle(img2, (0,0), (250,250), (0,0,0), -1)

### here black part 0 & white part is 1  

bitAND = cv2.bitwise_and(img2,img1)
bitOR = cv2.bitwise_or(img2,img1)
bitXOR = cv2.bitwise_xor(img2,img1)
bitNOT = cv2.bitwise_not(img2)                      ### NOT reverse the format



cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAND", bitAND)
cv2.imshow("bitOR", bitOR)
cv2.imshow("bitXOR", bitXOR)
cv2.imshow("bitNOT", bitNOT)




cv2.waitKey(0)
cv2.destroyAllWindows()