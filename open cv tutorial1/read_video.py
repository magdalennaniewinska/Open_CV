import cv2 as cv

# Define a video capture object
capture = cv.VideoCapture("/Users/magdalenan/Open_CV/Open_CV/Source/Videos/dog.mp4")

while True:

    # Capture video frame by frame
    isTrue, frame = capture.read()

    # Display the resulting frame
    cv.imshow("Video", frame)

    # The 'q' button is set as the quiting button
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# After the loop release the capture object
capture.release()

# Destroy all the windows
cv.destroyAllWindows()
