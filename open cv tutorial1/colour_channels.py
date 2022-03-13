import cv2 as cv
import numpy as np

img = cv.imread("/Users/magdalenan/Open_CV/Open_CV/Source/Photos/park.jpeg")
cv.imshow("Park", img)

# split image into colour channels and display in gray scale
b, g, r = cv.split(img)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merge images
merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

# show only one colour
blank = np.zeros(img.shape[:2], dtype="uint8")

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue channel", blue)
cv.imshow("Green channel", green)
cv.imshow("Red channes", red)


cv.waitKey(0)