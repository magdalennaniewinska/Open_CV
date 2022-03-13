import cv2 as cv
import numpy as np

img = cv.imread("/Users/magdalenan/Open_CV/Open_CV/Source/Photos/park.jpeg")
cv.imshow("Park", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow("Sobel X", sobel_x)
cv.imshow("Sobel y", sobel_y)
cv.imshow("Sobel combined", combine_sobel)

# Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)


cv.waitKey(0)
