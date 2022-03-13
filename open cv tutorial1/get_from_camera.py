import cv2 as cv

# Define a video capture object
vid = cv.VideoCapture(0)

# Face detection classifier
haar_cascade = cv.CascadeClassifier("haar_face.xml")

while True:

    # Capture video frame by frame
    ret, frame = vid.read()

    # Face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    for (x, y, w, h) in faces_rectangle:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    # Display the resulting frame
    cv.imshow('frame', frame)

    # The 'q' button is set as the quiting button
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the capture object
vid.release()

# Destroy all the windows
cv.destroyAllWindows()