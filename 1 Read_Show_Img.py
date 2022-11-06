import cv2

### reading the image in numpy format
img = cv2.imread("lena.jpg",0)
print(img)

### show the image
cv2.imshow('image',img)

### adding wait keypip 
cv2.waitKey()
# cv2.destroyWindow()

### Write image / Copy
cv2.imwrite("lena_copy.png",img)
cv2.destroyWindow()


