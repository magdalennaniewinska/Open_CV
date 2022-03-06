import cv2 as cv
import numpy as np

img = cv.imread("Source/Photos/cats.jpeg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# mask in shape of circle in picture centre
# size of mask have to be the same as masked image
mask = cv.circle(blank, center=(img.shape[1]//2, img.shape[0]//2), radius=100, color=255, thickness=-1)

masked_image = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked image", masked_image)

cv.waitKey(0)
