import cv2
# cap = cv2.VideoCapture(0)     ## VideoCapture(0) for web cam
cap = cv2.VideoCapture("DoPal.mp4")   ## to show stored video


while (True):
    ret, frame = cap.read()
    # ret = True if frames available else False
    # frame = each frame wll be saved

    ## BGR to gray image
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))       ## to get the frame width and height
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


    cv2.imshow("frame", frame)
    # cv2.imshow("frame", gray)

    if cv2.waitKey(8) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow()