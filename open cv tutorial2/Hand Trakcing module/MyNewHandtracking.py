import cv2 as cv
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0

cap = cv.VideoCapture(0)
detector = htm.HandDetecteor()

while True:
    success, img = cap.read()
    detector.find_hands(img=img)
    lmList = detector.find_position(img, draw=False)
    if lmList:
        print(lmList[4])

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