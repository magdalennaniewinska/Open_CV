import cv2 as cv
import mediapipe as mp
import time


class PoseEstimator():
    def __init__(self, mode=False, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(static_image_mode=self.mode, min_detection_confidence=self.detection_confidence,
                                      min_tracking_confidence=self.tracking_confidence)

    def find_pose(self, img, draw=True):
        # Convert image
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # Use hands model
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        return img

    def find_position(self, img, draw=True):
        self.lm_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)

                # Transform landmarks to pixel values
                cx, cy = int(lm.x*w), int(lm.y*h)
                self.lm_list.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx,cy), 10, (255,0,0), cv.FILLED)
        return self.lm_list


def main():
    pTime = 0

    cap = cv.VideoCapture('PoseVideos/1.mp4')
    detector = PoseEstimator()

    while True:
        success, img = cap.read()
        img = detector.find_pose(img)
        lm_list = detector.find_position(img, draw=False)
        if len(lm_list) != 0:
            #print(lm_list[14])
            cv.circle(img, (lm_list[14][1], lm_list[14][2]), 10, (255, 0, 0), cv.FILLED)

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
