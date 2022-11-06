from asyncio import events
import cv2
import numpy as np

### getting all the events available in cv2 library

'''
events = [i for i in dir(cv2) if "EVENT" in i]
print(events) '''


'''
OUTPUT:
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON',
'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY',
'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP',
'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP',
'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL',
'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']'''

img = np.zeros([512,512,3])
cv2.imshow('image',img)

def mouse_click(event, x, y, flag, param):

    ### to check if left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:

        font = cv2.FONT_HERSHEY_COMPLEX
        # LB = 'Left Button'
        cor = str(y)+ "," + str(x)  ### to get the cordinats of image on each click

        cv2.putText(img, cor, (x,y), font, 1, (255,255,0),1)
        cv2.imshow("image",img)


    ### to check if right mouse botton was clicked
    if event == cv2.EVENT_RBUTTONDBLCLK:
        RB = 'Right Botton'
        cv2.putText(img, RB, (x,y), font, 1, (0,255,0),2)
        cv2.imshow("image",img)


cv2.setMouseCallback("image",mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()