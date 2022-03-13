import cv2 as cv

img = cv.imread("/Users/magdalenan/Open_CV/Open_CV/Source/Photos/cats.jpeg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# simple thresholding
threshold, thresh = cv.threshold(gray, thresh=150, maxval=255, type=cv.THRESH_BINARY)
cv.imshow("Simple thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, thresh=150, maxval=255, type=cv.THRESH_BINARY_INV)
cv.imshow("Simple thresholded inverse", thresh_inv)

# adaptive thresholding - let computer to find threshold value
adaptive_threshold = cv.adaptiveThreshold(gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
                                          thresholdType=cv.THRESH_BINARY, blockSize=13, C=9)
cv.imshow("Adaptive thresholding", adaptive_threshold)

cv.waitKey(0)
