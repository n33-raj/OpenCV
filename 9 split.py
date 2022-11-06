from gettext import npgettext
import cv2
import numpy as np

img = cv2.imread("messi5.jpg")


print(img.shape)
print(img.size)
print(img.dtype)


''' NOW LETS COPY THE BALL N THE PIC FROM ONE PLACE TO OTHER '''

### finding the cordinates of the ball 

"""
def mouse_click(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_COMPLEX
        cor = str(x)+ "," + str(y) 
        cv2.putText(img, cor, (x,y), font, 1, (255,255,0),1)
        cv2.imshow("image",img)
cv2.imshow("image",img)
cv2.setMouseCallback('image',mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows() 
"""


b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))

### we get the cordinates as (x1,y1) & (x2,y2) top left corner & lower right corner (280:340) & (330:390])
ball = img[280:340 , 330:390]     ### these cordinates must be accurate and in order (y2,y1) & (x2,x1)

### now placing the ball on other cordinates
img[273:333, 100:160] = ball    

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()