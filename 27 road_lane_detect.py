import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread("road.png")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cap = cv2.VideoCapture("Driving.mp4")

### putting this inside a func so that it can be used easily
def process(img):      
    print(img.shape)

    height = img.shape[0]
    width = img.shape[1]

    ### finding region of intrest (ROI)
    region_of_int = [(0, height), (width/2, height/2), (width, height)]

    ### MASK everything except ROI
    def roi(image, vertices):
        mask = np.zeros_like(image)
        # channel_count = image.shape[2]
        match_mask_color = 255
        cv2.fillPoly(mask, vertices, match_mask_color)
        masked_image = cv2.bitwise_and(image, mask)
        return masked_image

    ### Edge detection
    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 50, 200)

    final_image = roi(canny_image, np.array([region_of_int], np.int32))

    ### using HoughlineP
    lines = cv2.HoughLinesP(final_image, 2, np.pi/180, 100, minLineLength=5, maxLineGap=25)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1,y1), (x2,y2), (0,255,0),5)

    return img
    # plt.imshow(img)
    # plt.show()


while (cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)     ### calling func
    cv2.imshow("frames",frame)

    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


'''
Steps:
    1. find ROI with the help of shape method
    2. MASK everything except ROI
    3. Edge detection using Canny/Thershold
    4. HoughLineP
'''