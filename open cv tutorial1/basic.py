import cv2 as cv

img = cv.imread("/Users/magdalenan/Open_CV/Open_CV/Source/Photos/cat.jpeg")
cv.imshow("Cat", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
#cv.imshow("Canny", canny)

canny_blur = cv.Canny(blur, 125, 175)
#cv.imshow("Canny_blur", canny_blur)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow("Eroded", eroded)

# Resize
resize = cv.resize(img, (500,500))
#cv.imshow("Resize", resize)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
