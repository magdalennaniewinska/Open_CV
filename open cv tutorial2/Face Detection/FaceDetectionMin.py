import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture('FaceVideos/3.mp4')
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
face_detection = mpFaceDetection.FaceDetection(0.75)


while True:
    success, img = cap.read()

    # Convert image
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Face detection
    results = face_detection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            # print(id, detection)
            # print(detection.score)
            # Default function to drawing
            # mpDraw.draw_detection(img, detection)

            # Transform landmarks to pixel values
            h, w, c = img.shape
            bbox_from_class = detection.location_data.relative_bounding_box
            bbox = int(bbox_from_class.xmin * w), int(bbox_from_class.ymin * h),\
                   int(bbox_from_class.width * w), int(bbox_from_class.height * h)
            cv.rectangle(img, bbox, (255,0,255), 2)
            cv.putText(img, f"{(int(detection.score[0]*100))}%", (bbox[0], bbox[1] - 20), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

    # Measure FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display img
    cv.putText(img, f"FPS:{(int(fps))}", (100, 100), cv.FONT_HERSHEY_COMPLEX_SMALL, 7, (255, 0, 0), 2)
    cv.imshow("Image", img)
    # The 'q' button is set as the quiting button
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
