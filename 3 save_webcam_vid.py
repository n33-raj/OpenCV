import cv2
cap = cv2.VideoCapture(0)     ## VideoCapture(0) for web cam
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("Output_vid.avi",fourcc,20.0,(640,480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        cv2.imshow("frame", frame)
        out.write(frame)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyWindow()
