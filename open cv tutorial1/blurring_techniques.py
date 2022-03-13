import cv2 as cv

img = cv.imread("/Users/magdalenan/Open_CV/Open_CV/Source/Photos/cats.jpeg")
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (5,5))
# numbers 3,3 determine window size, bigger window = more blurred image
cv.imshow("Average", average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (5,5), 0)
# gaussian average blur give certain weights to counting average
# so for the same window size we get less blurred image than with average method
cv.imshow("Gaussian", gauss)

# Median blur
median = cv.medianBlur(img, 3)
# median blur is effective with small number
cv.imshow("Median", median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
# the most effective, most used in advanced projects, apply blurring but edges stay
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
