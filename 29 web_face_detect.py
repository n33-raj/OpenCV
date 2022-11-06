import cv2
import matplotlib.pyplot as plt
import numpy as np

### using CascadeClassifier to read xml file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture("face.mp4")
while cap.isOpened():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ### face_cascade.detectMultiscale(image, scalefactor, miniNeighbors)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
