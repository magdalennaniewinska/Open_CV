import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("/Users/magdalenan/Open_CV/Open_CV/Source/Photos/park.jpeg")
cv.imshow("Boston", img)

# colour system is system of representing matrix of colours

# to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
cv.imshow("HSV", hsv)

# BRG to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("LAB", lab)

# open cv interpret images as BGR and matplotlib as RGB
plt.imshow(img)
# will show inverted colours
plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# will show inverted colours
cv.imshow("RGB", rgb)
# will show normal colours
plt.imshow(rgb)
plt.show()

cv.waitKey(0)