import cv2 as cv
import numpy as np

img = cv.imread("Source/Photos/cat.jpeg")
cv.imshow("Cat", img)


# Translations - shifting an image by x,y
def translate(img, x, y):
    # Create translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x -> Left
# x ->Right
# -y -> Up
# y -> Down

translated = translate(img, 100, 100)
cv.imshow("Translated", translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# Angle of rotation is counted anticlockwise
# to rotate clockwise pass angle with - so -45
rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Flipping
# 0 -> flipping vertically by x, 1 -> flip horizontally y, -1 -> flip verticallt and horizontally by 0.0
flip_vertical = cv.flip(img, 0)
cv.imshow("Vertical", flip_vertical)

flip_horizontal = cv.flip(img, 1)
cv.imshow("Horizontal", flip_horizontal)

flip_ver_and_hor = cv.flip(img, -1)
cv.imshow("Vertical and horizontal flip", flip_ver_and_hor)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)