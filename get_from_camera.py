import cv2 as cv

# Define a video capture object
vid = cv.VideoCapture(0)

while True:

    # Capture video frame by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv.imshow('frame', frame)

    # The 'q' button is set as the quiting button
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the capture object
vid.release()

# Destroy all the windows
cv.destroyAllWindows()