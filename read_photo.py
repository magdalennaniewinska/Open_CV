import cv2 as cv

### Reading photos

img = cv.imread("Source/Photos/cat.jpeg")

cv.imshow("Cat", img)

cv.waitKey(0)