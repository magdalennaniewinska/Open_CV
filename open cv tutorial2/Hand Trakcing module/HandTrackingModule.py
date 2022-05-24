import cv2 as cv
import mediapipe as mp
import time


class HandDetecteor():
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=self.mode, max_num_hands=self.max_hands,
                                         min_detection_confidence=self.detection_confidence,
                                         min_tracking_confidence=self.tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        # Convert image
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # Use hands model
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_no=0, draw=True):
        lmList = []

        if self.results.multi_hand_landmarks:
            me_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(me_hand.landmark):
                # Check height, width and channels
                h, w, c = img.shape
                # Check position of every landmark
                cx, cy = int(lm.x * w), int(lm.y * h)
                # Add positions to list
                lmList.append([id, cx, cy])

                if draw:
                    cv.circle(img, (cx, cy), 7, (255, 0, 255), cv.FILLED)
        return lmList


def main():
    pTime = 0

    cap = cv.VideoCapture(0)
    detector = HandDetecteor()

    while True:
        success, img = cap.read()
        detector.find_hands(img=img)
        lmList = detector.find_position(img)
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


if __name__ == "__main__":
    main()
