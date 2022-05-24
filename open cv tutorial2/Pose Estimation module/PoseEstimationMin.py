import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('PoseVideos/1.mp4')
pTime = 0

while True:
    success, img = cap.read()

    # Convert image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Pose detection
    result = pose.process(imgRGB)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = img.shape
            #print(id, lm)

            # Transform landmarks to pixel values
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)

    # Measure FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display img
    cv2.putText(img, str(int(fps)), (100, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 7, (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(10)