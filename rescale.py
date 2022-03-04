import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Function to rescale images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Function work only for live video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture("Source/Videos/dog.mp4")

while True:

    # Capture video frame by frame
    isTrue, frame = capture.read()

    # Rescale video
    frame_resized = rescaleFrame(frame)

    # Display the resulting frame
    cv.imshow("Video", frame)
    cv.imshow("Video_resized", frame_resized)

    # The 'q' button is set as the quiting button
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# After the loop release the capture object
capture.release()

# Destroy all the windows
cv.destroyAllWindows()
