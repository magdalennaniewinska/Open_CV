import cv2 as cv
import numpy as np

img = cv.imread("Source/Photos/cat.jpeg")
#cv.imshow("Cat", img)


# Creating blank image
# height, width, number of colour channels
blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow("Blank", blank)

# Paint the image by certain colour
blank[:] = 0,255,0
#cv.imshow("Green", blank)

# Paint part of image
blank[200:300, 300:400] = 0,0,255
#cv.imshow("Red", blank)

# Draw a rectangle
cv.rectangle(img, (300,150), (600,400), (0,0,255), thickness=2)
#cv.imshow("Rectangle", img)

# Fill rectangle by colour
cv.rectangle(img, (300,150), (600,400), (0,0,255), thickness=cv.FILLED)
#cv.imshow("Rectangle Filled", img)

# Instead of giving fixed values you can pass proportion
cv.rectangle(img, (0,0), (img.shape[1]//3, img.shape[0]//3), (0,0,255), thickness=-1)
#cv.imshow("Rectangle proportion", img)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
#cv.imshow("Circle", blank)

# Draw a line
cv.line(img, (0,0), (img.shape[1], img.shape[0]), (255,0,0), thickness=6)
#cv.imshow("Line", img)

# Write text
cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), thickness=2)
#cv.imshow("Text", blank)

cv.waitKey(0)