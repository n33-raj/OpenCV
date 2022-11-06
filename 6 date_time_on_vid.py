import cv2
import datetime

cap = cv2.VideoCapture(0)


# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while True:
    ret, frame = cap.read()

    date_time = str(datetime.datetime.now())
    fonts = cv2.FONT_HERSHEY_COMPLEX_SMALL
    frame = cv2.putText(frame,date_time,(0,30),fonts,1,(250,100,140),1)

    # cv2.putText()
    cv2.imshow("video",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cv2.release()
cv2.destroyAllWindows()
