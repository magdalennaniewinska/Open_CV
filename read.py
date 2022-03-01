import cv2 as cv

### Reading photos

# img = cv.imread("Resources/Photos/cat_large.jpeg")
#
# cv.imshow("Cat", img)
#
# cv.waitKey(0)

### Reading Video

capture = cv.VideoCapture("Source/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
