import cv2
import matplotlib.pyplot as plt
import numpy as np

### using CascadeClassifier to read xml file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


img = cv2.imread("tony.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

### face_cascade.detectMultiscale(image, scalefactor, miniNeighbors)
faces = face_cascade.detectMultiScale(gray, 1.3, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 4)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0,0,255), 2)



cv2.imshow("image", img)
cv2.waitKey()
