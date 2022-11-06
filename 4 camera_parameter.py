import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))       ## to get the frame width and height
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
 

cap.set(3,720)    ## here index are 3 & 4 becoz 1&2 are the orignal index of the frame
cap.set(4,1080)

print(cap.get(3))     ## or we can write the syntax for height & width, here we giving only index
print(cap.get(4))


print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        cv2.imshow('photo',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

