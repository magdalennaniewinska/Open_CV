import cv2 as cv

### Reading photos

img = cv.imread("/Users/magdalenan/Open_CV/Open_CV/Source/Photos/cat.jpeg")

cv.imshow("Cat", img)

cv.waitKey(0)