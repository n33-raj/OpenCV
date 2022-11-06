import cv2
import numpy as np

cap = cv2.VideoCapture("traffic.mp4")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)       ### using blur to mute the noise
    ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
    # thresh = cv2.Canny(blur, 50,200)
    dilate = cv2.dilate(thresh, None, iterations=5 )     ### to reemove the white noise
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
    # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)

    ### rectangle on the place of contours
    ### boundingRect used to draw an approximate rectangle around the binary image
    for i in contours:
        (x, y, w, h) = cv2.boundingRect(i)

        if cv2.contourArea(i) < 50:
            continue
        # else:
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(frame1, "Moment", (10,20), cv2.FONT_HERSHEY_COMPLEX_SMALL ,1, (0,0,255), 1)



    cv2.imshow("frame",frame1)
    frame1 = frame2
    ret, frame2 = cap.read()


    if cv2.waitKey(5) & 0xff == ord("x"):    ###cv2.waitKey(85) == 27 for Esc key
        break

cv2.destroyAllWindows()
cap.release()