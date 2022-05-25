import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture('FaceVideos/6.mp4')
pTime = 0

mpFaceMesh = mp.solutions.face_mesh
mpDraw = mp.solutions.drawing_utils
face_mesh = mpFaceMesh.FaceMesh(max_num_faces=2)

while True:
    success, img = cap.read()

    # Convert image
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Face detection
    results = face_mesh.process(imgRGB)

    if results.multi_face_landmarks:
        # print(results.multi_face_landmarks)
        for faceLm in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLm, mpFaceMesh.FACEMESH_CONTOURS)
            for id, lm in enumerate(faceLm.landmark):
                # Transform landmarks to pixel values
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)

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
