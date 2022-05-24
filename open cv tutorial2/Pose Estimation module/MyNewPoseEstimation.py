import cv2 as cv
import mediapipe as mp
import time
import PoseEstimationModule as pem

pTime = 0
cap = cv.VideoCapture('PoseVideos/2.mp4')
detector = pem.PoseEstimator()

while True:
    success, img = cap.read()
    img = detector.find_pose(img)
    lm_list = detector.find_position(img, draw=False)
    if len(lm_list) != 0:
        #print(lm_list[14])
        cv.circle(img, (lm_list[25][1], lm_list[25][2]), 10, (255, 0, 0), cv.FILLED)

    # Measure FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display img
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 255), 2)
    cv.imshow("Image", img)

    # The 'q' button is set as the quiting button
    if cv.waitKey(1) & 0xFF == ord('q'):
        break