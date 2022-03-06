import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Source/Photos/cats.jpeg")
cv.imshow("Cats", img)

# histograms allow to visualize pixels intensity of image

# histogram for gray scale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

gray_hist = cv.calcHist([gray], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("number of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])

# histogram for masked image
blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv.circle(blank, center=(img.shape[1]//2, img.shape[0]//2), radius=100, color=255, thickness=-1)

masked_image = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow("Masked image", masked_image)

gray_hist_masked = cv.calcHist([gray], channels=[0], mask=mask, histSize=[256], ranges=[0,256])

plt.figure()
plt.title("Grayscale Histogram with mask")
plt.xlabel("Bins")
plt.ylabel("number of pixels")
plt.plot(gray_hist_masked)
plt.xlim([0,256])

# histogram for colour image RGB
plt.figure()
plt.title("Colour Histogram")
plt.xlabel("Bins")
plt.ylabel("number of pixels")

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])


plt.show()

cv.waitKey(0)
