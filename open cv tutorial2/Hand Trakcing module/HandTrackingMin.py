import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

#
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    # Convert image
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Use hands model
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):

                # Check height, width and channels
                h, w, c = img.shape

                # Check position of every landmark
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Measure FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Display img
    cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX_SMALL, 3, (255,0,255), 2)
    cv.imshow("Image", img)

    # The 'q' button is set as the quiting button
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
