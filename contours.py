import cv2 as cv
import numpy as np

img = cv.imread("Source/Photos/cat.jpeg")
cv.imshow("Cats", img)

blank_canny = np.zeros(img.shape, dtype="uint8")
blank_threshold = np.zeros(img.shape, dtype="uint8")

# convert image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# detect edges
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank_canny, contours, -1, (0,0,255), 1)
cv.imshow("Contours draw canny", blank_canny)
print(f"{len(contours)} these many contours was found")

# second method - thresholding, taking  an image and change it to only binary values black or white
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank_threshold, contours, -1, (0,0,255), 1)
cv.imshow("Contours draw threshold", blank_threshold)
print(f"{len(contours)} these many contours was found")

cv.waitKey(0)